import argparse
import json
from pathlib import Path
from urllib import request


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Envia un prompt a la API local y guarda la respuesta JSON."
    )
    parser.add_argument("body_json", help="Archivo JSON con prompt, model y max_tokens.")
    parser.add_argument("output_json", help="Archivo donde se guardara la respuesta.")
    parser.add_argument(
        "--url",
        default="http://127.0.0.1:8000/api/chat",
        help="URL del endpoint de la API local.",
    )
    args = parser.parse_args()

    body_path = Path(args.body_json)
    out_path = Path(args.output_json)

    payload = json.loads(body_path.read_text(encoding="utf-8"))
    data = json.dumps(payload).encode("utf-8")

    req = request.Request(
        args.url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with request.urlopen(req, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Respuesta guardada en: {out_path}")


if __name__ == "__main__":
    main()
