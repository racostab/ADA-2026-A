#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jpgm
"""

import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    n = int(input_data[idx]); idx += 1
    mode = input_data[idx]; idx += 1

    man_to_id = {}
    woman_to_id = {}
    id_to_man = [None] * n
    id_to_woman = [None] * n

    raw_men_prefs = [[None] * n for _ in range(n)]
    raw_women_prefs = [[None] * n for _ in range(n)]

    for i in range(n):
        name = input_data[idx]; idx += 1
        man_to_id[name] = i
        id_to_man[i] = name
        for j in range(n):
            raw_men_prefs[i][j] = input_data[idx]; idx += 1

    for i in range(n):
        name = input_data[idx]; idx += 1
        woman_to_id[name] = i
        id_to_woman[i] = name
        for j in range(n):
            raw_women_prefs[i][j] = input_data[idx]; idx += 1

    men_pref = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            men_pref[i][j] = woman_to_id[raw_men_prefs[i][j]]

    women_pref = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            women_pref[i][j] = man_to_id[raw_women_prefs[i][j]]

    men_rank = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            woman_id = woman_to_id[raw_men_prefs[i][j]]
            men_rank[i][woman_id] = j

    women_rank = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            man_id = man_to_id[raw_women_prefs[i][j]]
            women_rank[i][man_id] = j

    partner_men = [-1] * n
    partner_women = [-1] * n
    
    if mode == 'w':
        women_next_proposal = [0] * n
        free_women = deque(range(n))

        while free_women:
            w = free_women[0]
            m = women_pref[w][women_next_proposal[w]]
            women_next_proposal[w] += 1

            if partner_women[m] == -1:
                partner_women[m] = w
                partner_men[w] = m
                free_women.popleft()
            else:
                current_w = partner_women[m]
                if men_rank[m][w] < men_rank[m][current_w]:
                    partner_women[m] = w
                    partner_men[w] = m
                    partner_men[current_w] = -1
                    free_women.popleft()
                    free_women.append(current_w)
                else:
                    free_women.popleft()
                    free_women.append(w)

        for w in range(n):
            print(f"{id_to_woman[w]} {id_to_man[partner_men[w]]}")

    else:
        men_next_proposal = [0] * n
        free_men = deque(range(n))

        while free_men:
            m = free_men[0]
            w = men_pref[m][men_next_proposal[m]]
            men_next_proposal[m] += 1

            if partner_men[w] == -1:
                partner_men[w] = m
                partner_women[m] = w
                free_men.popleft()
            else:
                current_m = partner_men[w]
                if women_rank[w][m] < women_rank[w][current_m]:
                    partner_men[w] = m
                    partner_women[m] = w
                    partner_women[current_m] = -1
                    free_men.popleft()
                    free_men.append(current_m)
                else:
                    free_men.popleft()
                    free_men.append(m)

        for m in range(n):
            print(f"{id_to_man[m]} {id_to_woman[partner_women[m]]}")

if __name__ == "__main__":
    main()
