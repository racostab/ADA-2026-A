# Author: Ronquillo Nunez Braulio
# Optional task: Landau notation

import sys


def normalize_polynomial(terms):
    polynomial = {}

    for coefficient, exponent in terms:
        if coefficient == 0:
            continue
        polynomial[exponent] = polynomial.get(exponent, 0.0) + coefficient

    return {exp: coef for exp, coef in polynomial.items() if coef != 0}


def dominant_term(polynomial):
    if not polynomial:
        return 0, 0.0

    exponent = max(polynomial)
    return exponent, polynomial[exponent]


def format_number(value):
    if value == int(value):
        return str(int(value))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def compare_landau(first, second):
    first = normalize_polynomial(first)
    second = normalize_polynomial(second)
    first_degree, first_coef = dominant_term(first)
    second_degree, second_coef = dominant_term(second)

    if not first and not second:
        return "f(n) = Theta(g(n))", "ambas funciones son cero"

    if not first:
        return "f(n) = O(g(n))", "f(n) es la funcion cero"

    if not second:
        return "g(n) = O(f(n))", "g(n) es la funcion cero"

    if first_degree == second_degree:
        ratio = first_coef / second_coef
        return "f(n) = Theta(g(n))", f"lim f(n)/g(n) = {format_number(ratio)}"

    if first_degree < second_degree:
        return "f(n) = O(g(n))", "lim f(n)/g(n) = 0"

    return "g(n) = O(f(n))", "lim f(n)/g(n) = infinito"


def read_polynomial(data, pos):
    term_count = int(data[pos])
    pos += 1
    terms = []

    for _ in range(term_count):
        coefficient = float(data[pos])
        exponent = int(data[pos + 1])
        pos += 2
        terms.append((coefficient, exponent))

    return terms, pos


def solve():
    data = sys.stdin.read().split()

    if not data:
        return

    first, pos = read_polynomial(data, 0)
    second, pos = read_polynomial(data, pos)

    relation, reason = compare_landau(first, second)
    print(relation)
    print(reason)


if __name__ == "__main__":
    solve()
