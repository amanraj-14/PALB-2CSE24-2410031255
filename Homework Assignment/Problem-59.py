from collections import Counter

def sort_freq(s):
    freq = Counter(s)
    res = sorted(s, key=lambda x: (freq[x], x))
    return ''.join(res)


# Input
s = "geeksforgeeks"

# Output
print(sort_freq(s))