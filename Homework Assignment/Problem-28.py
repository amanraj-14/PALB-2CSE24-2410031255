def search_matrix(matrix, target):
    if not matrix:
        return False

    n, m = len(matrix), len(matrix[0])
    left, right = 0, n * m - 1

    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // m][mid % m]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))