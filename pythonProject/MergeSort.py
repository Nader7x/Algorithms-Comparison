def merge(left, right, key_func):
    sorted_res = [None] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        # Changed the comparison to sort in descending order
        if key_func(left[i]) >= key_func(right[j]):
            sorted_res[k] = left[i]
            i += 1
        else:
            sorted_res[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        sorted_res[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sorted_res[k] = right[j]
        j += 1
        k += 1

    return sorted_res


def merge_sort(data, key_func):
    if len(data) <= 1:
        return data
    mid = len(data) // 2  # Mid value
    left = merge_sort(data[:mid], key_func)
    right = merge_sort(data[mid:], key_func)
    return merge(right, left, key_func)
