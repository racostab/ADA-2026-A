import argparse
import subprocess
import sys
from pathlib import Path


def normalize(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ejecuta una solucion Python y compara la salida con un archivo esperado."
    )
    parser.add_argument("program", help="Archivo .py a probar.")
    parser.add_argument("input_file", help="Archivo de entrada.")
    parser.add_argument("expected_file", help="Archivo con la salida esperada.")
    args = parser.parse_args()

    input_text = Path(args.input_file).read_text(encoding="utf-8")
    expected_text = Path(args.expected_file).read_text(encoding="utf-8")

    result = subprocess.run(
        [sys.executable, args.program],
        input=input_text,
        text=True,
        capture_output=True,
        timeout=20,
        check=False,
    )

    if result.returncode != 0:
        print("La solucion termino con error:")
        print(result.stderr)
        raise SystemExit(result.returncode)

    actual = normalize(result.stdout)
    expected = normalize(expected_text)

    if actual == expected:
        print("OK: la salida coincide con la esperada.")
        return

    print("FALLO: la salida no coincide.")
    print("\nEsperado:\n")
    print(expected)
    print("\nRecibido:\n")
    print(actual)
    raise SystemExit(1)


if __name__ == "__main__":
    main()
