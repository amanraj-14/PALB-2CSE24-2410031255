def largest_string(s, k):
    stack = []
    
    for ch in s:
        while stack and k > 0 and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    
    return ''.join(stack[:len(stack)-k])


# Input
s = "ritz"
k = 2

# Output
print(largest_string(s, k))