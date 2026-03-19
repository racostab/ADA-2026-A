import sys
from collections import deque

def gale_shapley(proposers_order, proposers_prefs, receivers_prefs):
    # ranking inverso para comparar en O(1)
    rank = {}
    for r, prefs in receivers_prefs.items():
        rank[r] = {p: i for i, p in enumerate(prefs)}

    free = deque(proposers_order)      # cola de proponentes libres
    engaged = {}                       # receiver -> proposer
    nxt = {p: 0 for p in proposers_order}

    while free:
        p = free.popleft()
        i = nxt[p]
        if i >= len(proposers_prefs[p]):
            continue

        r = proposers_prefs[p][i]
        nxt[p] = i + 1

        if r not in engaged:
            engaged[r] = p
        else:
            p2 = engaged[r]
            if rank[r][p] < rank[r][p2]:
                engaged[r] = p
                free.append(p2)
            else:
                free.append(p)

    return engaged  # receiver -> proposer


def solve_case(n, who, men_rows, women_rows):
    men_order = [row[0] for row in men_rows]
    women_order = [row[0] for row in women_rows]

    men_prefs = {row[0]: row[1:] for row in men_rows}
    women_prefs = {row[0]: row[1:] for row in women_rows}

    if who == 'm':
        engaged = gale_shapley(men_order, men_prefs, women_prefs)  # woman -> man
        man_to_woman = {m: w for w, m in engaged.items()}
        # salida: proposer primero, en orden de proposers (hombres)
        return [m + " " + man_to_woman[m] for m in men_order]

    # who == 'w'
    engaged = gale_shapley(women_order, women_prefs, men_prefs)    # man -> woman
    woman_to_man = {w: m for m, w in engaged.items()}
    # salida: proposer primero, en orden de proposers (mujeres)
    return [w + " " + woman_to_man[w] for w in women_order]


def main():
    lines = sys.stdin.read().splitlines()
    i = 0
    out = []

    while True:
        # saltar líneas vacías
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines):
            break

        first = lines[i].split()
        i += 1
        if len(first) < 2:
            break

        n = int(first[0])
        who = first[1]

        men_rows = []
        for _ in range(n):
            while i < len(lines) and not lines[i].strip():
                i += 1
            men_rows.append(lines[i].split())
            i += 1

        women_rows = []
        for _ in range(n):
            while i < len(lines) and not lines[i].strip():
                i += 1
            women_rows.append(lines[i].split())
            i += 1

        out.extend(solve_case(n, who, men_rows, women_rows))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()