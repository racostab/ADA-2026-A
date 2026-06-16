# Author: Ronquillo Nunez Braulio
# Optional task: limits for complexity comparison

import sys


RANKS = {
    "1": 0,
    "log_log_n": 1,
    "log_n": 2,
    "sqrt_n": 3,
    "n_1_2": 3,
    "n_minus_1": 4,
    "n": 4,
    "two_log_n": 4,
    "n_log_n": 5,
    "log_n_factorial": 5,
    "n_3_2": 6,
    "n_2": 7,
    "n2": 7,
    "n_2_log_n": 8,
    "n_3": 9,
    "two_n": 10,
    "pi_n": 11,
    "n_factorial": 12,
    "n_n": 13,
    "two_two_n": 14,
}


def solve():
    data = sys.stdin.read().split()

    if not data:
        return

    count = int(data[0])
    functions = data[1 : 1 + count]
    unknown = [name for name in functions if name not in RANKS]

    if unknown:
        print("funciones desconocidas:")
        print(" ".join(unknown))
        return

    groups = {}
    for name in functions:
        groups.setdefault(RANKS[name], []).append(name)

    print("orden_creciente =")
    for rank in sorted(groups):
        print(" = ".join(sorted(groups[rank])))


if __name__ == "__main__":
    solve()
