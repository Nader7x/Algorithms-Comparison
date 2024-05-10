def quick_sort(arr, key_func):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for item in arr:
        if key_func(item) < key_func(pivot):
            less_than_pivot.append(item)
        elif key_func(item) == key_func(pivot):
            equal_to_pivot.append(item)
        else:
            greater_than_pivot.append(item)
    return quick_sort(greater_than_pivot, key_func) + equal_to_pivot + quick_sort(less_than_pivot, key_func)
