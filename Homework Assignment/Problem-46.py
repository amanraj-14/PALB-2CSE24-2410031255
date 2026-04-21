def previous_greater(arr):
    stack = []
    result = []
    
    for x in arr:
        while stack and stack[-1] <= x:
            stack.pop()
        
        result.append(stack[-1] if stack else -1)
        stack.append(x)
    
    return result