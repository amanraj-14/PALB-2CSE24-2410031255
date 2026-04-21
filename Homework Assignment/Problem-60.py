def sort_by_length(arr):
    return sorted(arr, key=lambda x: len(x))


# Input
arr = ["GeeksforGeeks", "I", "from", "am"]

# Output
print(sort_by_length(arr))