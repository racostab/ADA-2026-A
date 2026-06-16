from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = isqrt(n)
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def nth_prime(target):
    count = 0
    candidate = 1

    while count < target:
        candidate += 1
        if is_prime(candidate):
            count += 1

    return candidate


def solve():
    return nth_prime(10001)


if __name__ == "__main__":
    print(solve())
