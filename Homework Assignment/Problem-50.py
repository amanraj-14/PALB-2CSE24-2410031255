def combinationSum3(k, n):
    res = []
    
    def backtrack(start, path, total):
        if len(path) == k and total == n:
            res.append(path[:])
            return
        
        for i in range(start, 10):
            if total + i > n:
                break
            backtrack(i+1, path + [i], total + i)
    
    backtrack(1, [], 0)
    return res