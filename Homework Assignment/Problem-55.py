def min_swaps(s1, s2):
    if len(s1) != len(s2):
        return -1
    
    ones = s1.count('1') + s2.count('1')
    if ones % 2 != 0:
        return -1
    
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    
    return diff // 2


# Input
s1 = "1100"
s2 = "1111"

# Output
print(min_swaps(s1, s2))
