from collections import Counter

def check_perm(txt, pat):
    k = len(pat)
    pat_count = Counter(pat)
    
    for i in range(len(txt)-k+1):
        if Counter(txt[i:i+k]) == pat_count:
            return True
    return False


# Input
txt = "geeks"
pat = "eke"

# Output
print(check_perm(txt, pat))