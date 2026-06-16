import argparse
import importlib.util
from pathlib import Path


CASES = {
    "numbers": [5, 1, 4, 2, 3],
    "strings": ["hola", "hello", "salut", "aloha", "namaste"],
    "duplicates": [3, 1, 2, 3, 1],
    "sorted": [1, 2, 3, 4, 5],
    "reverse": [9, 7, 5, 3, 1],
    "single": [42],
    "empty": [],
}


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("candidate_stupid_sort", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("No se pudo cargar el modulo.")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_sort_function(module):
    for name in ("gnome_sort", "stupid_sort", "sort"):
        candidate = getattr(module, name, None)
        if callable(candidate):
            return candidate, name
    raise RuntimeError("No se encontro una funcion gnome_sort, stupid_sort o sort.")


def main():
    parser = argparse.ArgumentParser(description="Valida una implementacion de Stupid/Gnome Sort.")
    parser.add_argument("program", help="Archivo Python generado por Claude.")
    parser.add_argument("--case", choices=sorted(CASES), required=True)
    args = parser.parse_args()

    module = load_module(Path(args.program))
    sort_function, function_name = find_sort_function(module)
    original = CASES[args.case]
    data = list(original)
    expected = sorted(original)
    actual = sort_function(data)

    if actual is None:
        actual = data

    if list(actual) != expected:
        print(f"FALLO: {function_name} no ordeno el caso {args.case}.")
        print(f"Esperado: {expected}")
        print(f"Recibido: {actual}")
        raise SystemExit(1)

    if original and data != original and actual is not data:
        print("FALLO: la funcion modifico la entrada aunque devolvio una lista distinta.")
        raise SystemExit(1)

    print(f"OK: {function_name} ordena correctamente el caso {args.case}.")


if __name__ == "__main__":
    main()
