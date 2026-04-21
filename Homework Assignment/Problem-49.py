def max_visible(arr):
    n = len(arr)
    
    def count_visible(i):
        count = 1
        
        # left
        max_h = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] < max_h:
                count += 1
            else:
                break
        
        # right
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                count += 1
            else:
                break
        
        return count
    
    return max(count_visible(i) for i in range(n))