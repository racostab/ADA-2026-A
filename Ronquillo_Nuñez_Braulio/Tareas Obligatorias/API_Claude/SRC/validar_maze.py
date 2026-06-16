import argparse
import subprocess
import sys
from collections import deque
from pathlib import Path


DIRS = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}
ORDER = ["U", "R", "D", "L"]


def parse_case(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    header = list(map(int, lines[0].split()))
    rows, cols, sr, sc, tr, tc, output_type = header
    maze = lines[1 : 1 + rows]
    return rows, cols, sr, sc, tr, tc, output_type, maze


def is_open(maze, r, c):
    return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == " "


def shortest_distance(maze, sr, sc, tr, tc):
    if not is_open(maze, sr, sc) or not is_open(maze, tr, tc):
        return None

    q = deque([(sr, sc, 0)])
    seen = {(sr, sc)}

    while q:
        r, c, d = q.popleft()
        if (r, c) == (tr, tc):
            return d

        for step in ORDER:
            dr, dc = DIRS[step]
            nr, nc = r + dr, c + dc
            if is_open(maze, nr, nc) and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))

    return None


def validate_path(maze, sr, sc, tr, tc, path):
    if not is_open(maze, sr, sc) or not is_open(maze, tr, tc):
        return False, "La fuente o el destino no estan sobre una celda transitable."

    r, c = sr, sc
    for ch in path:
        if ch not in DIRS:
            return False, f"Direccion invalida: {ch}"
        dr, dc = DIRS[ch]
        r += dr
        c += dc
        if not is_open(maze, r, c):
            return False, "El camino sale del laberinto o atraviesa una pared."

    if (r, c) != (tr, tc):
        return False, "El camino no termina en el destino."

    return True, "Camino valido."


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Valida una solucion de Maze contra un caso de prueba."
    )
    parser.add_argument("program", help="Archivo .py de la solucion.")
    parser.add_argument("input_file", help="Archivo de entrada del problema.")
    parser.add_argument(
        "--allow-any-path",
        action="store_true",
        help="Acepta cualquier camino valido para O=3, aunque no sea el mas corto.",
    )
    args = parser.parse_args()

    input_path = Path(args.input_file)
    input_text = input_path.read_text(encoding="utf-8")
    rows, cols, sr, sc, tr, tc, output_type, maze = parse_case(input_path)
    _ = rows, cols

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

    output = result.stdout.strip()
    dist = shortest_distance(maze, sr, sc, tr, tc)
    exists = dist is not None

    if output_type == 1:
        expected = "True" if exists else "False"
        if output == expected:
            print("OK: la respuesta booleana es correcta.")
            return
        print(f"FALLO: se esperaba {expected} y se recibio {output!r}.")
        raise SystemExit(1)

    if output_type == 2:
        if dist is None:
            print("FALLO: no existe camino y la salida no puede ser una longitud.")
            raise SystemExit(1)
        if output == str(dist):
            print("OK: la longitud coincide con la del camino mas corto.")
            return
        print(
            "FALLO: la longitud no coincide con la del camino mas corto "
            f"(esperada {dist}, recibida {output!r})."
        )
        raise SystemExit(1)

    if output_type == 3:
        ok, message = validate_path(maze, sr, sc, tr, tc, output)
        if not ok:
            print(f"FALLO: {message}")
            raise SystemExit(1)

        if args.allow_any_path:
            print("OK: el camino es valido.")
            return

        if dist is not None and len(output) == dist:
            print("OK: el camino es valido y ademas es de longitud minima.")
            return

        print(
            "FALLO: el camino llega al destino, pero no tiene longitud minima. "
            f"Longitud del camino: {len(output)}. Longitud minima: {dist}."
        )
        raise SystemExit(1)

    print(f"Tipo de salida no soportado: {output_type}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
