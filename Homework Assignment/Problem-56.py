def min_add(s):
    balance = 0
    add = 0
    
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                add += 1
    
    return add + balance


# Input
s = "(()("

# Output
print(min_add(s))