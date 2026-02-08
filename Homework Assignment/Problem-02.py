arr = [1, 4, 3, 5, 8, 6]

min_val = arr[0]
max_val = arr[0]

for i in arr:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print(min_val, max_val)
