"""P1"""
def init_db(raw_db):
    """DB as id_s"""
    keys = [r[0] for r in raw_db]
    keys_as_id = {k: i for i, k in enumerate(keys)}
    prefs_as_id = [[keys_as_id[k] for k in r[1:]] for r in raw_db]
    return prefs_as_id,  keys

def get_entities(n, who):
    """Entities as id_s"""
    is_m = int(who == 'M')# ==1 0_n !=1 n_2n
    s = list(range((1-is_m)*n, (2 - is_m)*n))
    p = list(range(is_m*n, (1+is_m)*n))
    return s, p

def solve_match(s, p, couples, ranking):
    """Get rejected Suitor or None"""
    curr = couples[p]
    if curr == -1:
        couples[p] = s
        return None
    if ranking[p][s] < ranking[p][curr]:
        couples[p] = s
        return curr
    return s

def stable_matching(n, who, raw_db):
    """G-S"""
    prefs, keys = init_db(raw_db)
    suitors, prospects = get_entities(n, who)
    p_ranking, couple = {}, {}
    for p in prospects:
        p_ranking[p] = {pid: r for r, pid in enumerate(prefs[p])}
        couple[p] = -1
    proposals = {s: 0 for s in suitors}
    free_s = list(suitors)#Free suitors
    while free_s:
        s = free_s.pop(0)
        p = prefs[s][proposals[s]]
        proposals[s] += 1
        reject = solve_match(s, p, couple, p_ranking)
        if reject is not None:
            free_s.append(reject)
    res = {s: p for p, s in couple.items()}
    #order by suitors
    print("\n".join([f"{keys[s]} {keys[res[s]]}" for s in suitors]))

if __name__ == '__main__':
    aux = input().split()
    t, w = int(aux[0]), aux[1].upper()
    pref = [input().strip().split() for _ in range(t*2)]
    stable_matching(t, w, pref)
