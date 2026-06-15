import json
import math
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .extraer_codigo import extract_code


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PROJECT_ROOT / "DAT" / "runs"
GENERATED_DIR = PROJECT_ROOT / "DAT" / "generated"
DEFAULT_MODEL = "claude-sonnet-4-5"


@dataclass(frozen=True)
class TestCase:
    label: str
    args: list[str]
    level: str


def pass_at_k(total: int, correct: int, k: int) -> float:
    if total <= 0:
        return 0.0
    if correct <= 0:
        return 0.0
    if total - correct < k:
        return 1.0

    return 1.0 - math.comb(total - correct, k) / math.comb(total, k)


def run_command(args: list[str], timeout: int = 25) -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, *args],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    output = (result.stdout + result.stderr).strip()
    return result.returncode == 0, output


def maze_tests(program_path: Path) -> list[TestCase]:
    program = str(program_path)
    return [
        TestCase("Maze sample O=1", ["SRC/validar_maze.py", program, "DAT/tests/maze_sample_o1.in"], "@3"),
        TestCase("Maze sample O=2", ["SRC/validar_maze.py", program, "DAT/tests/maze_sample_o2.in"], "@3"),
        TestCase("Maze sample O=3", ["SRC/validar_maze.py", program, "DAT/tests/maze_sample_o3.in"], "@3"),
        TestCase("Maze no path O=1", ["SRC/validar_maze.py", program, "DAT/tests/maze_no_path_o1.in"], "@5"),
        TestCase("Maze source = target O=1", ["SRC/validar_maze.py", program, "DAT/tests/maze_same_cell_o1.in"], "@5"),
        TestCase("Maze source = target O=2", ["SRC/validar_maze.py", program, "DAT/tests/maze_same_cell_o2.in"], "@5"),
        TestCase("Maze source = target O=3", ["SRC/validar_maze.py", program, "DAT/tests/maze_same_cell_o3.in"], "@5"),
        TestCase("Maze another shortest path O=3", ["SRC/validar_maze.py", program, "DAT/tests/maze_alt_path_o3.in"], "@5"),
    ]


def stupid_sort_tests(program_path: Path) -> list[TestCase]:
    program = str(program_path)
    return [
        TestCase("Numeros desordenados", ["SRC/validar_stupid_sort.py", program, "--case", "numbers"], "@3"),
        TestCase("Cadenas desordenadas", ["SRC/validar_stupid_sort.py", program, "--case", "strings"], "@3"),
        TestCase("Duplicados", ["SRC/validar_stupid_sort.py", program, "--case", "duplicates"], "@5"),
        TestCase("Ya ordenado", ["SRC/validar_stupid_sort.py", program, "--case", "sorted"], "@5"),
        TestCase("Orden inverso", ["SRC/validar_stupid_sort.py", program, "--case", "reverse"], "@5"),
        TestCase("Un elemento", ["SRC/validar_stupid_sort.py", program, "--case", "single"], "@5"),
        TestCase("Lista vacia", ["SRC/validar_stupid_sort.py", program, "--case", "empty"], "@5"),
    ]


ALGORITHMS: dict[str, dict[str, object]] = {
    "maze": {
        "title": "Maze",
        "prompt": (
            "Solve this competitive programming problem in Python 3. Read from standard input "
            "and write to standard output. Return only one ```python``` code block and nothing else. "
            "Problem: Given a maze as a rectangular matrix, find a path from source (Sr, Sc) to target "
            "(Tr, Tc). The maze uses space as corridor and # as wall. Moves are only U, R, D, L. "
            "Input: first line has R C Sr Sc Tr Tc O. Then come R lines of the maze. "
            "Output depends on O: 1 -> print True or False depending on whether a path exists. "
            "2 -> print the length of the shortest path. 3 -> print one shortest path as a string "
            "of U, R, D, L, breaking ties by exploring neighbors in the order U, R, D, L. "
            "Use BFS and make the program robust for large inputs."
        ),
        "max_tokens": 1200,
        "tests": maze_tests,
    },
    "stupid_sort": {
        "title": "Stupid/Gnome Sort",
        "prompt": (
            "Write a Python 3 implementation of Gnome Sort, also known in this project as Stupid Sort. "
            "Return only one ```python``` code block and nothing else. The code must define a function "
            "gnome_sort(values) that receives a list of comparable values and returns a new sorted list "
            "without modifying the original list. Include a small main block that reads whitespace-separated "
            "tokens from stdin and prints them sorted in one line, but the function is the main requirement."
        ),
        "max_tokens": 700,
        "tests": stupid_sort_tests,
    },
}


MOCK_SOLUTIONS = {
    "maze": """from collections import deque
import sys

DIRS = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]

def main():
    header = sys.stdin.readline().split()
    if not header:
        return
    r, c, sr, sc, tr, tc, o = map(int, header)
    maze = [sys.stdin.readline().rstrip('\\n') for _ in range(r)]
    if maze[sr][sc] != ' ' or maze[tr][tc] != ' ':
        print(False if o == 1 else (-1 if o == 2 else ''))
        return
    q = deque([(sr, sc)])
    parent = {(sr, sc): None}
    move = {}
    while q:
        cr, cc = q.popleft()
        if (cr, cc) == (tr, tc):
            break
        for dr, dc, ch in DIRS:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < r and 0 <= nc < c and maze[nr][nc] == ' ' and (nr, nc) not in parent:
                parent[(nr, nc)] = (cr, cc)
                move[(nr, nc)] = ch
                q.append((nr, nc))
    found = (tr, tc) in parent
    if o == 1:
        print('True' if found else 'False')
    elif o == 2:
        if not found:
            print(-1)
        else:
            cur = (tr, tc)
            dist = 0
            while parent[cur] is not None:
                dist += 1
                cur = parent[cur]
            print(dist)
    else:
        if not found:
            print('')
        else:
            cur = (tr, tc)
            path = []
            while parent[cur] is not None:
                path.append(move[cur])
                cur = parent[cur]
            print(''.join(reversed(path)))

if __name__ == '__main__':
    main()
""",
    "stupid_sort": """def gnome_sort(values):
    result = list(values)
    index = 0
    while index < len(result):
        if index == 0 or result[index - 1] <= result[index]:
            index += 1
        else:
            result[index - 1], result[index] = result[index], result[index - 1]
            index -= 1
    return result

if __name__ == '__main__':
    import sys
    print(' '.join(gnome_sort(sys.stdin.read().split())))
""",
}


def call_claude(client, prompt: str, model: str, max_tokens: int) -> str:
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    text = ""
    for block in message.content:
        if getattr(block, "type", None) == "text":
            text += block.text
    return text


def evaluate_program(algorithm: str, program_path: Path) -> dict:
    tests_factory = ALGORITHMS[algorithm]["tests"]
    tests = tests_factory(program_path)  # type: ignore[operator]
    details = []

    for test in tests:
        ok, output = run_command(test.args)
        details.append(
            {
                "label": test.label,
                "level": test.level,
                "ok": ok,
                "message": output.splitlines()[0] if output else "",
            }
        )

    at3_tests = [test for test in details if test["level"] == "@3"]
    all_tests = details
    at3_passed = sum(1 for test in at3_tests if test["ok"])
    all_passed = sum(1 for test in all_tests if test["ok"])
    reaches_at3 = at3_passed == len(at3_tests)
    reaches_at5 = all_passed == len(all_tests)

    return {
        "tests": details,
        "at3_passed": at3_passed,
        "at3_total": len(at3_tests),
        "at5_passed": all_passed,
        "at5_total": len(all_tests),
        "reaches_at3": reaches_at3,
        "reaches_at5": reaches_at5,
        "grade": "@5" if reaches_at5 else ("@3" if reaches_at3 else "sin nivel"),
    }


def run_attempt(
    algorithm: str,
    attempt_number: int,
    run_dir: Path,
    client=None,
    model: str = DEFAULT_MODEL,
    mock: bool = False,
) -> dict:
    config = ALGORITHMS[algorithm]
    prompt = str(config["prompt"])
    max_tokens = int(config["max_tokens"])
    started = time.perf_counter()

    if mock:
        response_text = f"```python\n{MOCK_SOLUTIONS[algorithm]}\n```"
    else:
        if client is None:
            raise RuntimeError("No hay cliente de Claude disponible.")
        response_text = call_claude(client, prompt, model, max_tokens)

    code = extract_code(response_text)
    algorithm_dir = run_dir / algorithm
    algorithm_dir.mkdir(parents=True, exist_ok=True)
    program_path = algorithm_dir / f"attempt_{attempt_number:02d}.py"
    response_path = algorithm_dir / f"attempt_{attempt_number:02d}.json"
    program_path.write_text(code, encoding="utf-8")
    response_path.write_text(
        json.dumps(
            {
                "algorithm": algorithm,
                "attempt": attempt_number,
                "model": model,
                "mock": mock,
                "response": response_text,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    evaluation = evaluate_program(algorithm, program_path)
    elapsed_ms = round((time.perf_counter() - started) * 1000, 2)

    return {
        "attempt": attempt_number,
        "algorithm": algorithm,
        "algorithm_title": config["title"],
        "model": model,
        "mock": mock,
        "elapsed_ms": elapsed_ms,
        "program_path": str(program_path.relative_to(PROJECT_ROOT)),
        "response_path": str(response_path.relative_to(PROJECT_ROOT)),
        **evaluation,
    }


def summarize_attempts(algorithm: str, attempts: list[dict]) -> dict:
    total = len(attempts)
    at3_correct = sum(1 for item in attempts if item["reaches_at3"])
    at5_correct = sum(1 for item in attempts if item["reaches_at5"])

    return {
        "algorithm": algorithm,
        "algorithm_title": ALGORITHMS[algorithm]["title"],
        "attempts": total,
        "at3_correct": at3_correct,
        "at5_correct": at5_correct,
        "at3_rate": round(at3_correct / total, 4) if total else 0.0,
        "at5_rate": round(at5_correct / total, 4) if total else 0.0,
        "pass_at_3": round(pass_at_k(total, at5_correct, 3), 4),
        "pass_at_5": round(pass_at_k(total, at5_correct, 5), 4),
    }


def run_evaluation(
    algorithms: list[str],
    attempts: int = 10,
    client=None,
    model: str = DEFAULT_MODEL,
    mock: bool = False,
) -> dict:
    run_id = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:8]
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    summaries = []

    for algorithm in algorithms:
        algorithm_results = []
        for attempt in range(1, attempts + 1):
            try:
                result = run_attempt(
                    algorithm=algorithm,
                    attempt_number=attempt,
                    run_dir=run_dir,
                    client=client,
                    model=model,
                    mock=mock,
                )
            except Exception as exc:
                result = {
                    "attempt": attempt,
                    "algorithm": algorithm,
                    "algorithm_title": ALGORITHMS[algorithm]["title"],
                    "model": model,
                    "mock": mock,
                    "elapsed_ms": 0,
                    "program_path": "",
                    "response_path": "",
                    "tests": [],
                    "at3_passed": 0,
                    "at3_total": 0,
                    "at5_passed": 0,
                    "at5_total": 0,
                    "reaches_at3": False,
                    "reaches_at5": False,
                    "grade": "error",
                    "error": str(exc),
                }
            algorithm_results.append(result)
            results.append(result)
        summaries.append(summarize_attempts(algorithm, algorithm_results))

    report = {
        "run_id": run_id,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model": model,
        "attempts_per_algorithm": attempts,
        "mock": mock,
        "summaries": summaries,
        "results": results,
    }

    report_path = run_dir / "report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report
