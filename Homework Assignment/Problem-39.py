def subsets(nums):
    result = [[]]

    for num in nums:
        result += [curr + [num] for curr in result]

    return result


print(subsets([1,2,3]))
print(subsets([0]))