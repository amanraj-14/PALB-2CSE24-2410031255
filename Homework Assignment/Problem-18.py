arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

i = j = k = 0
n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)

result = []

while i < n1 and j < n2 and k < n3:
    if arr1[i] == arr2[j] == arr3[k]:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
        j += 1
        k += 1
    else:
        minimum = min(arr1[i], arr2[j], arr3[k])
        if arr1[i] == minimum:
            i += 1
        elif arr2[j] == minimum:
            j += 1
        else:
            k += 1

if result:
    print(result)
else:
    print([-1])
