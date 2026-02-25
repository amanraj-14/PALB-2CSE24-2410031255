def three_way_partition(arr, a, b):
    start = 0
    end = len(arr) - 1
    i = 0

    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1

    return arr


print(three_way_partition([1, 4, 3, 6, 2, 1], 1, 3))