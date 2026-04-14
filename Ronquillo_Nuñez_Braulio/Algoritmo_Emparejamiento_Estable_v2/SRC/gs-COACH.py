# Autor: Braulio Ronquillo
# version 2
import sys
from collections import deque

def gale_shapley(proposers_order, proposers_prefs, receivers_prefs):
    # ranking inverso para comparar en O(1)
    rank = {
        r: {p: i for i, p in enumerate(prefs)} for r, prefs in receivers_prefs.items()
    }
    free = deque(proposers_order)  # cola de proponentes libres
    engaged = {}  # receiver -> proposer
    nxt = {p: 0 for p in proposers_order}
    while free:
        p = free.popleft()
        prefs = proposers_prefs[p]
        i = nxt[p]
        if i >= len(prefs):
            continue

        r = prefs[i]  # nxt evita repetir propuestas y con eso no hay ciclos infinitos
        nxt[p] = i + 1

        p2 = engaged.get(r)
        if p2 is None:
            engaged[r] = p
        elif rank[r][p] < rank[r][p2]:
            engaged[r] = p
            free.append(p2)
        else:
            free.append(p)

    return engaged  # receiver -> proposer


def next_nonempty_tokens(stream):
    for line in stream:
        parts = line.split()
        if parts:
            return parts
    return None


def read_cases(stream):
    while True:
        first = next_nonempty_tokens(stream)
        if first is None:
            return

        if len(first) < 2:
            raise ValueError("Cada caso debe iniciar con: N lado_proponente")

        n = int(first[0])
        who = first[1].lower()

        men_rows = []
        for _ in range(n):
            row = next_nonempty_tokens(stream)
            if row is None:
                raise ValueError("Faltan filas del conjunto de hombres")
            men_rows.append(row)

        women_rows = []
        for _ in range(n):
            row = next_nonempty_tokens(stream)
            if row is None:
                raise ValueError("Faltan filas del conjunto de mujeres")
            women_rows.append(row)
        yield n, who, men_rows, women_rows


def solve_case(n, who, men_rows, women_rows):
    men_order = [row[0] for row in men_rows]
    women_order = [row[0] for row in women_rows]

    men_prefs = {row[0]: row[1:] for row in men_rows}
    women_prefs = {row[0]: row[1:] for row in women_rows}

    if who == "m":
        engaged = gale_shapley(men_order, men_prefs, women_prefs)  # woman -> man
        man_to_woman = {m: w for w, m in engaged.items()}
        return [f"{m} {man_to_woman[m]}" for m in men_order]

    engaged = gale_shapley(women_order, women_prefs, men_prefs)  # man -> woman
    woman_to_man = {w: m for m, w in engaged.items()}
    return [f"{w} {woman_to_man[w]}" for w in women_order]


def main():
    first_line = True
    for n, who, men_rows, women_rows in read_cases(sys.stdin):
        for line in solve_case(n, who, men_rows, women_rows):
            if not first_line:
                sys.stdout.write("\n")
            sys.stdout.write(line)
            first_line = False

if __name__ == "__main__":
    main()
