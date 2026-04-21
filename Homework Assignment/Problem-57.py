def score_parentheses(s):
    stack = [0]
    
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            val = stack.pop()
            stack[-1] += max(2*val, 1)
    
    return stack[0]


# Input
s = "(()(()))"

# Output
print(score_parentheses(s))