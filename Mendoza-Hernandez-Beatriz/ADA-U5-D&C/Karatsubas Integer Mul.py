import sys

lines = sys.stdin.read().strip().splitlines()

t = int(lines[0])
idx = 1

for _ in range(t):
    line = lines[idx].strip()
    idx += 1

    if ' ' in line:
        a, b = line.split()
    else:
        a = line
        b = lines[idx].strip()
        idx += 1

    a = a.replace('_', '')
    b = b.replace('_', '')

    print(bin(int(a, 2) * int(b, 2))[2:])