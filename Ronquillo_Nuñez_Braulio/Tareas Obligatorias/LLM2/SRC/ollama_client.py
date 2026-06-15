from urllib import request, error
import json


def check_ollama(base_url: str, timeout: int = 3) -> dict:
    url = base_url.rstrip("/") + "/api/tags"
    req = request.Request(url, method="GET")

    try:
        with request.urlopen(req, timeout=timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
    except error.URLError as exc:
        return {
            "available": False,
            "error": "No se pudo conectar con Ollama. Revisa `ollama serve`.",
            "details": str(exc),
            "models": [],
        }

    models = [item.get("name", "") for item in result.get("models", [])]
    return {
        "available": True,
        "error": "",
        "details": "",
        "models": models,
    }


def ask_ollama(base_url: str, model: str, prompt: str, timeout: int = 180) -> str:
    url = base_url.rstrip("/") + "/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
    except error.URLError as exc:
        raise RuntimeError(
            "No se pudo conectar con Ollama. Revisa que este corriendo con `ollama serve`."
        ) from exc

    if "error" in result:
        raise RuntimeError(result["error"])

    return result.get("response", "").strip()
