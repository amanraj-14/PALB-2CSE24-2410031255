def time_to_seconds(t):
    h, m, s = map(int, t.split(":"))
    return h*3600 + m*60 + s


def min_diff(arr):
    times = sorted(time_to_seconds(t) for t in arr)
    
    ans = float('inf')
    
    for i in range(1, len(times)):
        ans = min(ans, times[i] - times[i-1])
    
    # circular
    ans = min(ans, 86400 - times[-1] + times[0])
    
    return ans


# Input
arr = ["00:00:01", "23:59:59", "00:00:05"]

# Output
print(min_diff(arr))