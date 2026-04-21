
def count_subarrays(arr):
    n = len(arr)
    stack = []
    res = 0
    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        
        if not stack:
            res += i + 1
        else:
            res += i - stack[-1]
        
        stack.append(i)
    
    return res