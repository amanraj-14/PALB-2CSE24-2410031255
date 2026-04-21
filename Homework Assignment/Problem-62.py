from collections import Counter

def winner(arr):
    freq = Counter(arr)
    max_votes = max(freq.values())
    
    candidates = [name for name in freq if freq[name] == max_votes]
    return [min(candidates), str(max_votes)]


# Input
arr = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john"]

# Output
print(winner(arr))