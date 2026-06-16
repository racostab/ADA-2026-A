import json
import os
import time
from urllib import error, parse, request

from .config import BASE_DIR


def load_local_env() -> None:
    env_path = BASE_DIR / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key and key not in os.environ:
            os.environ[key] = value


def _api_key(provider: dict) -> str:
    load_local_env()
    env_name = provider.get("api_key_env", "")
    return os.environ.get(env_name, "")


def _post_json(url: str, payload: dict, headers: dict, timeout: int) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {body}") from exc
    except error.URLError as exc:
        raise RuntimeError(str(exc)) from exc


def _post_json_with_retries(
    url: str,
    payload: dict,
    headers: dict,
    timeout: int,
    retry_attempts: int,
    retry_wait_seconds: int,
) -> dict:
    last_error = None

    for attempt in range(retry_attempts + 1):
        try:
            return _post_json(url, payload, headers, timeout)
        except RuntimeError as exc:
            last_error = exc
            message = str(exc)
            is_transient = "HTTP 503" in message or "UNAVAILABLE" in message or "HTTP 429" in message

            if not is_transient or attempt == retry_attempts:
                raise

            time.sleep(retry_wait_seconds)

    raise last_error if last_error else RuntimeError("Error desconocido al llamar la API.")


def check_providers(config: dict) -> dict:
    providers = config.get("llm", {}).get("providers", {})
    status = {}

    for provider_id, provider in providers.items():
        env_name = provider.get("api_key_env", "")
        has_key = bool(_api_key(provider))
        status[provider_id] = {
            "available": has_key,
            "label": provider.get("label", provider_id),
            "api_key_env": env_name,
            "message": "API key configurada." if has_key else f"Falta configurar {env_name}.",
        }

    return status


def ask_model(config: dict, model: dict, prompt: str, timeout: int) -> str:
    provider_id = model["provider"]
    provider = config["llm"]["providers"][provider_id]
    key = _api_key(provider)

    if not key:
        raise RuntimeError(f"Falta API key: configura {provider.get('api_key_env')}.")

    if provider_id == "openai":
        return _ask_openai(provider, model["model"], prompt, key, timeout)
    if provider_id == "mistral":
        return _ask_mistral(provider, model["model"], prompt, key, timeout)
    if provider_id == "gemini":
        return _ask_gemini(provider, model["model"], prompt, key, timeout)
    if provider_id == "claude":
        return _ask_claude(provider, model["model"], prompt, key, timeout)

    raise RuntimeError(f"Proveedor no soportado: {provider_id}")


def _ask_openai(provider: dict, model_name: str, prompt: str, key: str, timeout: int) -> str:
    url = provider.get("base_url", "https://api.openai.com/v1").rstrip("/") + "/responses"
    payload = {
        "model": model_name,
        "input": prompt,
        "max_output_tokens": int(provider.get("max_output_tokens", 1800)),
    }
    result = _post_json(url, payload, {"Authorization": f"Bearer {key}"}, timeout)

    if result.get("output_text"):
        return result["output_text"].strip()

    chunks = []
    for item in result.get("output", []):
        for content in item.get("content", []):
            text = content.get("text")
            if text:
                chunks.append(text)

    return "\n".join(chunks).strip()


def _ask_mistral(provider: dict, model_name: str, prompt: str, key: str, timeout: int) -> str:
    url = provider.get("base_url", "https://api.mistral.ai/v1").rstrip("/") + "/chat/completions"
    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": float(provider.get("temperature", 0.2)),
        "max_tokens": int(provider.get("max_output_tokens", 4000)),
    }
    result = _post_json(url, payload, {"Authorization": f"Bearer {key}"}, timeout)

    chunks = []
    for choice in result.get("choices", []):
        content = choice.get("message", {}).get("content", "")
        if content:
            chunks.append(content)

    return "\n".join(chunks).strip()


def _ask_gemini(provider: dict, model_name: str, prompt: str, key: str, timeout: int) -> str:
    base_url = provider.get("base_url", "https://generativelanguage.googleapis.com/v1beta")
    model_path = parse.quote(model_name, safe="")
    url = f"{base_url.rstrip('/')}/models/{model_path}:generateContent?key={parse.quote(key)}"
    generation_config = {
        "temperature": float(provider.get("temperature", 0.2)),
        "maxOutputTokens": int(provider.get("max_output_tokens", 1800)),
    }
    contents = [
        {
            "role": "user",
            "parts": [{"text": prompt}],
        }
    ]
    max_continuations = int(provider.get("max_continuations", 0))
    retry_attempts = int(provider.get("retry_attempts", 0))
    retry_wait_seconds = int(provider.get("retry_wait_seconds", 3))
    responses = []

    for attempt in range(max_continuations + 1):
        payload = {
            "contents": contents,
            "generationConfig": generation_config,
        }
        result = _post_json_with_retries(
            url,
            payload,
            {},
            timeout,
            retry_attempts,
            retry_wait_seconds,
        )
        text, finish_reason = _extract_gemini_text(result)

        if text:
            responses.append(text)

        if finish_reason != "MAX_TOKENS" or not text:
            break

        contents.append(
            {
                "role": "model",
                "parts": [{"text": text}],
            }
        )
        contents.append(
            {
                "role": "user",
                "parts": [
                    {
                        "text": (
                            "Continua exactamente desde donde se corto la respuesta anterior. "
                            "No repitas introduccion ni contenido ya escrito."
                        )
                    }
                ],
            }
        )

    return "\n\n".join(responses).strip()


def _extract_gemini_text(result: dict) -> tuple[str, str]:
    chunks = []
    finish_reason = ""
    for candidate in result.get("candidates", []):
        finish_reason = candidate.get("finishReason", finish_reason)
        for part in candidate.get("content", {}).get("parts", []):
            text = part.get("text")
            if text:
                chunks.append(text)

    return "\n".join(chunks).strip(), finish_reason


def _ask_claude(provider: dict, model_name: str, prompt: str, key: str, timeout: int) -> str:
    url = provider.get("base_url", "https://api.anthropic.com/v1").rstrip("/") + "/messages"
    payload = {
        "model": model_name,
        "max_tokens": int(provider.get("max_output_tokens", 1800)),
        "temperature": float(provider.get("temperature", 0.2)),
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }
    headers = {
        "x-api-key": key,
        "anthropic-version": provider.get("anthropic_version", "2023-06-01"),
    }
    result = _post_json(url, payload, headers, timeout)

    chunks = []
    for content in result.get("content", []):
        if content.get("type") == "text" and content.get("text"):
            chunks.append(content["text"])

    return "\n".join(chunks).strip()
