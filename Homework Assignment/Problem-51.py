def tug_of_war(arr):
    n = len(arr)
    total = sum(arr)
    target = total // 2
    
    dp = {0: []}
    
    for num in arr:
        new_dp = dict(dp)
        for s in dp:
            if s + num not in dp:
                new_dp[s + num] = dp[s] + [num]
        dp = new_dp
    
    best = max(s for s in dp if s <= target)
    subset1 = dp[best]
    subset2 = arr[:]
    
    for x in subset1:
        subset2.remove(x)
    
    return subset1, subset2