def count_balanced(arr):
    def value(s):
        vowels = "aeiou"
        v = sum(1 for c in s if c in vowels)
        c = len(s) - v
        return v - c
    
    prefix = [0]
    
    for s in arr:
        prefix.append(prefix[-1] + value(s))
    
    from collections import Counter
    freq = Counter(prefix)
    
    count = 0
    for x in freq:
        f = freq[x]
        count += f*(f-1)//2
    
    return count


# Input
arr = ["aeio", "aa", "bc", "ot", "cdbd"]

# Output
print(count_balanced(arr))