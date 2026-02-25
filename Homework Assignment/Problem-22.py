def smallest_subarray(x, arr):
    n = len(arr)
    min_len = n + 1
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return min_len if min_len != n + 1 else 0


# Test Cases
print(smallest_subarray(51, [1, 4, 45, 6, 0, 19]))
print(smallest_subarray(100, [1, 10, 5, 2, 7]))