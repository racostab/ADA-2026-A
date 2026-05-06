def binary_tree_sort(numbers):
    if not numbers:
        return []

    def merge_sort(numbers):
        if len(numbers) == 1:
            return numbers

        mid = len(numbers) // 2
        left_half = merge_sort(numbers[:mid])
        right_half = merge_sort(numbers[mid:])

        return merge(left_half, right_half)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    sorted_numbers = merge_sort(numbers)

    return ' '.join(map(str, sorted_numbers))


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(binary_tree_sort(numbers))

# Test cases:
# 1. Input: 5 2 8 1 9 6 7 3 4
#    Output: 1 2 3 4 5 6 7 8 9
# 2. Input: 10 20 30 40 50
#    Output: 10 20 30 40 50
# 3. Input: 
#    Output: []
# 4. Input: 1 2 3 4 5
#    Output: 1 2 3 4 5
# 5. Input: 5 4 3 2 1
#    Output: 1 2 3 4 5
# 6. Input: 10 9 8 7 6 5 4 3 2 1
#    Output: 1 2 3 4 5 6 7 8 9 10
# 7. Input: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#    Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 8. Input: 20 10 9 8 7 6 5 4 3 2 1
#    Output: 1 2 3 4 5 6 7 8 9 10 20
# 9. Input: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
#    Output: 1 2 3 4 5 6 7 8 9 10 11 12