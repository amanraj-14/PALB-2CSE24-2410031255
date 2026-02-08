nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):
    rem = target - num
    if rem in seen:
        print([seen[rem], i])
        break
    seen[num] = i
