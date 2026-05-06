import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_command(args):
    result = subprocess.run(
        [sys.executable, *args],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
    )
    ok = result.returncode == 0
    output = (result.stdout + result.stderr).strip()
    return ok, output


def print_result(label, ok, output):
    status = "OK" if ok else "FALLO"
    print(f"[{status}] {label}")
    if output:
        first_line = output.splitlines()[0]
        print(f"      {first_line}")


def evaluate_suite(title, tests):
    print(title)
    passed = 0
    for label, args in tests:
        ok, output = run_command(args)
        if ok:
            passed += 1
        print_result(label, ok, output)
    total = len(tests)
    print(f"Resumen: {passed}/{total}\n")
    return passed, total


def grade(passed, total):
    if passed == total:
        return "@5"
    if passed > 0:
        return "@3"
    return "sin nivel"


def main():
    combinations_at3 = [
        (
            "Combinations sample 1",
            [
                "SRC/probar_solucion.py",
                "SRC/soluciones/combinations.py",
                "DAT/tests/combinations_case1.in",
                "DAT/tests/combinations_case1.out",
            ],
        ),
        (
            "Combinations sample 2",
            [
                "SRC/probar_solucion.py",
                "SRC/soluciones/combinations.py",
                "DAT/tests/combinations_case2.in",
                "DAT/tests/combinations_case2.out",
            ],
        ),
    ]
    combinations_at5_extra = [
        (
            "Combinations singleton",
            [
                "SRC/probar_solucion.py",
                "SRC/soluciones/combinations.py",
                "DAT/tests/combinations_case3_single.in",
                "DAT/tests/combinations_case3_single.out",
            ],
        ),
        (
            "Combinations duplicates",
            [
                "SRC/probar_solucion.py",
                "SRC/soluciones/combinations.py",
                "DAT/tests/combinations_case4_duplicates.in",
                "DAT/tests/combinations_case4_duplicates.out",
            ],
        ),
        (
            "Combinations R = N",
            [
                "SRC/probar_solucion.py",
                "SRC/soluciones/combinations.py",
                "DAT/tests/combinations_case5_all.in",
                "DAT/tests/combinations_case5_all.out",
            ],
        ),
    ]

    maze_at3 = [
        (
            "Maze sample O=1",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_sample_o1.in",
            ],
        ),
        (
            "Maze sample O=2",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_sample_o2.in",
            ],
        ),
        (
            "Maze sample O=3",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_sample_o3.in",
            ],
        ),
    ]
    maze_at5_extra = [
        (
            "Maze no path O=1",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_no_path_o1.in",
            ],
        ),
        (
            "Maze source = target O=1",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_same_cell_o1.in",
            ],
        ),
        (
            "Maze source = target O=2",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_same_cell_o2.in",
            ],
        ),
        (
            "Maze source = target O=3",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_same_cell_o3.in",
            ],
        ),
        (
            "Maze another shortest path O=3",
            [
                "SRC/validar_maze.py",
                "SRC/soluciones/maze.py",
                "DAT/tests/maze_alt_path_o3.in",
            ],
        ),
    ]

    c3_passed, c3_total = evaluate_suite("Combinations @3", combinations_at3)
    c5_passed, c5_total = evaluate_suite(
        "Combinations @5", combinations_at3 + combinations_at5_extra
    )
    m3_passed, m3_total = evaluate_suite("Maze @3", maze_at3)
    m5_passed, m5_total = evaluate_suite("Maze @5", maze_at3 + maze_at5_extra)

    print("Calificacion propuesta")
    print(f"Combinations: {grade(c5_passed, c5_total)} ({c5_passed}/{c5_total})")
    print(f"Maze: {grade(m5_passed, m5_total)} ({m5_passed}/{m5_total})")
    print()
    print("Suposicion usada:")
    print("@3 = pasa los casos oficiales del enunciado.")
    print("@5 = pasa los oficiales y casos borde adicionales.")
    print()
    print("Detalle rapido:")
    print(f"Combinations oficiales: {c3_passed}/{c3_total}")
    print(f"Maze oficiales: {m3_passed}/{m3_total}")


if __name__ == "__main__":
    main()
