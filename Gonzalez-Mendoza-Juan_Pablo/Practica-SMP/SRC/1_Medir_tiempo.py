#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: jpgm
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from collections import deque

def main():
    t0_total = time.perf_counter()

    t0 = time.perf_counter()
    input_data = sys.stdin.read().split()
    t_lectura_stdin = time.perf_counter() - t0

    if not input_data:
        return

    idx = 0
    n    = int(input_data[idx]); idx += 1
    mode = input_data[idx];      idx += 1


    t0 = time.perf_counter()
    man_to_id   = {}
    woman_to_id = {}
    id_to_man   = [None] * n
    id_to_woman = [None] * n

    raw_proposer_prefs  = [[None] * n for _ in range(n)]
    raw_receiver_prefs  = [[None] * n for _ in range(n)]
    t_init_estructuras = time.perf_counter() - t0


    t0 = time.perf_counter()
    if mode == 'm':
        for i in range(n):
            name = input_data[idx]; idx += 1
            man_to_id[name]  = i
            id_to_man[i]     = name
            for j in range(n):
                raw_proposer_prefs[i][j] = input_data[idx]; idx += 1

        for i in range(n):
            name = input_data[idx]; idx += 1
            woman_to_id[name] = i
            id_to_woman[i]    = name
            for j in range(n):
                raw_receiver_prefs[i][j] = input_data[idx]; idx += 1

    else:  # mode == 'w'
        for i in range(n):
            name = input_data[idx]; idx += 1
            woman_to_id[name] = i
            id_to_woman[i]    = name
            for j in range(n):
                raw_proposer_prefs[i][j] = input_data[idx]; idx += 1

        for i in range(n):
            name = input_data[idx]; idx += 1
            man_to_id[name]  = i
            id_to_man[i]     = name
            for j in range(n):
                raw_receiver_prefs[i][j] = input_data[idx]; idx += 1
    t_lectura_prefs = time.perf_counter() - t0

    # ── Conversión nombres → IDs ───────────────────────────────────────────────
    t0 = time.perf_counter()
    if mode == 'm':
        proposer_pref  = [[woman_to_id[raw_proposer_prefs[i][j]]  for j in range(n)] for i in range(n)]
        receiver_rank  = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                man_id = man_to_id[raw_receiver_prefs[i][j]]
                receiver_rank[i][man_id] = j
    else:
        proposer_pref  = [[man_to_id[raw_proposer_prefs[i][j]]    for j in range(n)] for i in range(n)]
        receiver_rank  = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                woman_id = woman_to_id[raw_receiver_prefs[i][j]]
                receiver_rank[i][woman_id] = j
    t_conversion = time.perf_counter() - t0

    t0 = time.perf_counter()
    partner_of_receiver = [-1] * n
    partner_of_proposer = [-1] * n
    next_proposal       = [0]  * n

    free_proposers = deque(range(n))

    while free_proposers:
        p = free_proposers[0]
        r = proposer_pref[p][next_proposal[p]]
        next_proposal[p] += 1

        if partner_of_receiver[r] == -1:
            partner_of_receiver[r] = p
            partner_of_proposer[p] = r
            free_proposers.popleft()
        else:
            current_p = partner_of_receiver[r]
            if receiver_rank[r][p] < receiver_rank[r][current_p]:
                partner_of_receiver[r]        = p
                partner_of_proposer[p]         = r
                partner_of_proposer[current_p] = -1
                free_proposers.popleft()
                free_proposers.append(current_p)
            else:
                free_proposers.popleft()
                free_proposers.append(p)
    t_gale_shapley = time.perf_counter() - t0

    t0 = time.perf_counter()
    if mode == 'm':
        for p in range(n):
            print(f"{id_to_man[p]} {id_to_woman[partner_of_proposer[p]]}")
    else:
        for p in range(n):
            print(f"{id_to_woman[p]} {id_to_man[partner_of_proposer[p]]}")
    t_salida = time.perf_counter() - t0

    t_total = time.perf_counter() - t0_total

    tareas = [
        ("Lectura stdin",         t_lectura_stdin),
        ("Init estructuras",      t_init_estructuras),
        ("Lectura preferencias",  t_lectura_prefs),
        ("Conversion nombres→ID", t_conversion),
        ("Gale-Shapley",          t_gale_shapley),
        ("Salida",                t_salida),
        ("TOTAL",                 t_total),
    ]

    print("\n", file=sys.stderr)
    print(f"{'='*55}", file=sys.stderr)
    print(f"  Tiempos de ejecución  |  n={n}  modo={'H-proponen' if mode=='m' else 'M-proponen'}", file=sys.stderr)
    print(f"{'='*55}", file=sys.stderr)
    print(f"  {'Tarea':<26} {'Tiempo (s)':>10}  {'%':>6}", file=sys.stderr)
    print(f"  {'-'*44}", file=sys.stderr)
    for nombre, t in tareas[:-1]:
        pct = (t / t_total * 100) if t_total > 0 else 0
        print(f"  {nombre:<26} {t:>10.6f}  {pct:>5.1f}%", file=sys.stderr)
    print(f"  {'-'*44}", file=sys.stderr)
    nombre, t = tareas[-1]
    print(f"  {nombre:<26} {t:>10.6f}  {'100.0%':>6}", file=sys.stderr)
    print(f"{'='*55}", file=sys.stderr)


if __name__ == "__main__":
    main()
