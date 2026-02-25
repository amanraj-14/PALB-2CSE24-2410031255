def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path)
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return result


print(combination_sum([2,3,6,7], 7))
print(combination_sum([2,3,5], 8))
print(combination_sum([2], 1))