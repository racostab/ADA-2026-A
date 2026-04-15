from array import array
from math import isqrt


LIMIT = 100_000_000


def primes_up_to(limit: int) -> array:
    if limit < 2:
        return array("I")

    size = (limit - 1) // 2
    sieve = bytearray(b"\x01") * size
    cross_limit = isqrt(limit)

    for index in range((cross_limit - 3) // 2 + 1):
        if not sieve[index]:
            continue

        prime = 2 * index + 3
        start = (prime * prime - 3) // 2
        sieve[start::prime] = b"\x00" * (((size - start - 1) // prime) + 1)

    primes = array("I", [2])
    primes.extend(2 * index + 3 for index, is_prime in enumerate(sieve) if is_prime)
    return primes


def count_semiprimes(limit: int) -> int:
    max_prime = (limit - 1) // 2
    primes = primes_up_to(max_prime)

    total = 0
    right = len(primes) - 1

    for left, prime in enumerate(primes):
        if prime * prime >= limit:
            break

        while prime * primes[right] >= limit:
            right -= 1

        if right < left:
            break

        total += right - left + 1

    return total


def solve() -> int:
    return count_semiprimes(LIMIT)


if __name__ == "__main__":
    print(solve())
