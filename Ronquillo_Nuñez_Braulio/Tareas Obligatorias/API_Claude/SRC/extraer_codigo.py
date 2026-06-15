import argparse
import json
import re
from pathlib import Path


PYTHON_BLOCK_RE = re.compile(r"```python\s*(.*?)```", re.DOTALL | re.IGNORECASE)
ANY_BLOCK_RE = re.compile(r"```[a-zA-Z0-9_+-]*\s*(.*?)```", re.DOTALL)


def extract_code(text: str) -> str:
    python_blocks = PYTHON_BLOCK_RE.findall(text)
    if python_blocks:
        return python_blocks[0].strip() + "\n"

    any_blocks = ANY_BLOCK_RE.findall(text)
    if any_blocks:
        return any_blocks[0].strip() + "\n"

    return text.strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extrae un bloque de codigo de un JSON de respuesta y lo guarda en .py."
    )
    parser.add_argument("response_json", help="Archivo JSON con la respuesta de la API.")
    parser.add_argument("output_py", help="Archivo .py de salida.")
    args = parser.parse_args()

    response_path = Path(args.response_json)
    output_path = Path(args.output_py)

    data = json.loads(response_path.read_text(encoding="utf-8"))
    text = data.get("response", "")
    code = extract_code(text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(code, encoding="utf-8")
    print(f"Codigo guardado en: {output_path}")


if __name__ == "__main__":
    main()
