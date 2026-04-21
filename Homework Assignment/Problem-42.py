def footpath_cost(matrix, queries):
    n = len(matrix)
    m = len(matrix[0])
    results = []

    for r, c in queries:
        r -= 1  # convert to 0-based
        c -= 1
        
        mins = []

        # Top-left
        if r > 0 and c > 0:
            mins.append(min(matrix[i][j] for i in range(r) for j in range(c)))

        # Top-right
        if r > 0 and c < m-1:
            mins.append(min(matrix[i][j] for i in range(r) for j in range(c+1, m)))

        # Bottom-left
        if r < n-1 and c > 0:
            mins.append(min(matrix[i][j] for i in range(r+1, n) for j in range(c)))

        # Bottom-right
        if r < n-1 and c < m-1:
            mins.append(min(matrix[i][j] for i in range(r+1, n) for j in range(c+1, m)))

        results.append(sum(mins))

    return results