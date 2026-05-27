def counting_sort(lst):
    max_val = max(lst)
    if max_val == 0:
        return lst

    min_val = min(lst)
    max_val += 1

    count = [0] * max_val
    for num in lst:
        count[num] += 1

    sorted_lst = []
    for i in range(len(count)):
        sorted_lst.extend([i] * count[i])

    return sorted_lst