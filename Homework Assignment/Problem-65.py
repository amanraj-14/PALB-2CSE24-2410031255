import math
from collections import Counter

def count_vowel_strings(s):
    vowels = "aeiou"
    freq = Counter(s)
    
    total = 1
    count = 0
    
    for v in vowels:
        if freq[v] > 0:
            total *= freq[v]
            count += 1
    
    return total * math.factorial(count)


# Input
s = "aacidf"

# Output
print(count_vowel_strings(s))