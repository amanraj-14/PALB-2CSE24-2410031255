def min_swaps(arr, k):
    n = len(arr)
    count = sum(1 for num in arr if num <= k)

    bad = sum(1 for i in range(count) if arr[i] > k)
    ans = bad

    for i in range(n - count):
        if arr[i] > k:
            bad -= 1
        if arr[i + count] > k:
            bad += 1
        ans = min(ans, bad)

    return ans


print(min_swaps([2, 1, 5, 6, 3], 3))
print(min_swaps([2, 7, 9, 5, 8, 7, 4], 6))
print(min_swaps([2, 4, 5, 3, 6, 1, 8], 6))