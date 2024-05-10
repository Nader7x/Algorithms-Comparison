def bubble_sort(arr, key_func):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(arr[j]) < key_func(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
