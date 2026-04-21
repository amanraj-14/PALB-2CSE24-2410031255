from collections import Counter

def even_letters(s):
    freq = Counter(s)
    return sum(1 for x in freq if freq[x] % 2 == 0)


# Input
s = "abacaba"

# Output
print(even_letters(s))