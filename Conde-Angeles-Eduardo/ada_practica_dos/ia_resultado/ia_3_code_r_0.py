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
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

    sorted_numbers = merge_sort(numbers)

    return ' '.join(map(str, sorted_numbers))


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(binary_tree_sort(numbers))

# Test cases:
# 1. Input: 5 3 8 1 6 4 7 2
# 2. Input: 9 8 7 6 5 4 3 2 1
# 3. Input: 1 2 3 4 5 6 7 8 9
# 4. Input: 10 9 8 7 6 5 4 3 2 1
# 5. Input: 1 2 3 4 5 6 7 8 9 10
# 6. Input: 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2