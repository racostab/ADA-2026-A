"""Permutations P2"""
def p_n_r(r, data, aux):
    """Permute from n r"""
    if len(aux) == r:
        print(" ".join(aux))
        return
    for i, val in enumerate(data):
        #filter by index
        remaining = data[:i] + data[i+1:]
        aux.append(val)
        p_n_r(r, remaining, aux)
        aux.pop()

if __name__ == '__main__':
    ps = input().split(" ")
    n = int(ps[0])
    c_r = int(ps[1])
    u = input().split(" ")
    p_n_r(c_r, u, [])
