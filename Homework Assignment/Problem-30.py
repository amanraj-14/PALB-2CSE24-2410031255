def row_with_max_ones(arr):
    max_row = -1
    max_count = 0

    for i in range(len(arr)):
        count = arr[i].count(1)
        if count > max_count:
            max_count = count
            max_row = i

    return max_row


print(row_with_max_ones([[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]))
print(row_with_max_ones([[0,0],[1,1]]))
print(row_with_max_ones([[0,0],[0,0]]))