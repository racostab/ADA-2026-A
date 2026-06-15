#Author: Braulio Alberto Ronquillo Nunez
LIMIT_DIGITS = 9


def count_even_length_reversible(digits: int) -> int:
    return 20 * pow(30, digits // 2 - 1)


def count_odd_length_reversible(digits: int) -> int:
    return 100 * pow(500, (digits - 3) // 4)


def count_reversible_with_digits(digits: int) -> int:
    if digits % 2 == 0:
        return count_even_length_reversible(digits)
    if digits % 4 == 3:
        return count_odd_length_reversible(digits)
    return 0


def solve() -> int:
    return sum(count_reversible_with_digits(digits) for digits in range(1, LIMIT_DIGITS + 1))


if __name__ == "__main__":
    print(solve())
