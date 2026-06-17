import sys
n = len(list(map(int, sys.argv[1].split(','))))
m = int.bit_length(n)
asc = [0] * (2 ** m)
desc = [0] * (2 ** m)

for i in range(0, n):
    index = 2 ** m - 1 - (i % (2 ** m))
    asc[index] = int(sys.argv[1].split(',')[i])

for i in range(0, 2 ** m // 2 + 1):
    for j in range(i * 2, min((i + 1) * 2, n)):
        if asc[2 * i] > asc[2 * i + 1]:
            asc[2 * i], asc[2 * i + 1] = asc[2 * i + 1], asc[2 * i]

for i in range(0, 2 ** m // 2 + 1):
    for j in range(i * 2, min((i + 1) * 2, n)):
        if desc[2 * i] < desc[2 * i + 1]:
            desc[2 * i], desc[2 * i + 1] = desc[2 * i + 1], desc[2 * i]

output = []
for i in range(0, n):
    index = 2 ** m - 1 - (i % (2 ** m))
    output.append(str(int(desc[index])))

print(','.join(output))