def shortest_substring(s1, s2):
    required = set(s1)
    n = len(s2)
    
    left = 0
    count = {}
    formed = 0
    min_len = float('inf')
    
    for right in range(n):
        ch = s2[right]
        if ch in required:
            count[ch] = count.get(ch, 0) + 1
            if count[ch] == 1:
                formed += 1
        
        while formed == len(required):
            min_len = min(min_len, right-left+1)
            
            if s2[left] in required:
                count[s2[left]] -= 1
                if count[s2[left]] == 0:
                    formed -= 1
            left += 1
    
    return min_len if min_len != float('inf') else -1


# Input
s1 = "ae"
s2 = "acbaudeq"

# Output
print(shortest_substring(s1, s2))