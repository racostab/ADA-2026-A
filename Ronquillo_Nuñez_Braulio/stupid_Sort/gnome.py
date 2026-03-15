# Gnome Sort COMBINATIONS
# Ronquillo Braulio


def gnome_sort(arr):
    a = arr[:]
    i = 0
    n = len(a)

    while i < n:
        if i == 0 or a[i - 1] <= a[i]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]

        return a


def generate_combinations(arr, r):
    result = []
    current = []

    def bactrack(start):
        if len(current) == r:
            result.append(" ".join(current))
            return
        needed = r - len(current)
        limit = len(arr) - needed + 1

        for i in range(start, limit):
            current.append(arr[i])
            bactrack(i + 1)
            current.pop()

    bactrack(0)
    return result


def solve(data: str) -> str:
    lines = [line.strip() for line in data.strip().splitlines() if line.strip()]
    if len(lines) < 2:
        return ""

    n, r = map(int, lines[0].split())
    arr = lines[1].split()

    arr = arr[:n]

    if r > n or r <= 0:
        return ""

    arr = gnome_sort(arr)

    combos = generate_combinations(arr, r)
    return "\n".join(combos)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    print(solve(data))
