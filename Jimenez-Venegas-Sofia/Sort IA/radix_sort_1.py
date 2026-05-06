def radix_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    exponents = len(str(max_val))

    for exp in range(exponents):
        count_arr = [0] * 10
        output_arr = [0] * len(arr)

        for i in range(len(arr)):
            count_arr[(arr[i] // (10 ** exp) % 10)] += 1

        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]

        index = len(arr) - 1
        while index >= 0:
            rem = (arr[index] // (10 ** exp)) % 10
            count_arr[rem] -= 1
            output_arr[count_arr[rem]] = arr[index]
            index -= 1

        temp = arr
        arr = output_arr
        output_arr = temp

    return arr