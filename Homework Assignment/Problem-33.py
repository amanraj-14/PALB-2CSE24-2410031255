def combination_sum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path)
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            backtrack(i+1, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return result


print(combination_sum2([10,1,2,7,6,1,5], 8))
print(combination_sum2([2,5,2,1,2], 5))