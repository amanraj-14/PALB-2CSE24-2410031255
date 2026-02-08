arr1 = [1, 1, 1, 2, 2, 2]
arr2 = [1, 1, 2, 2, 2]
arr3 = [1, 1, 1, 1, 2, 2, 2, 2]

i = j = k = 0
n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)

ans = []

while i < n1 and j < n2 and k < n3:
    if arr1[i] == arr2[j] == arr3[k]:
        if not ans or ans[-1] != arr1[i]:
            ans.append(arr1[i])
        val = arr1[i]
        while i < n1 and arr1[i] == val:
            i += 1
        while j < n2 and arr2[j] == val:
            j += 1
        while k < n3 and arr3[k] == val:
            k += 1
    else:
        minimum = min(arr1[i], arr2[j], arr3[k])
        if arr1[i] == minimum:
            i += 1
        elif arr2[j] == minimum:
            j += 1
        else:
            k += 1

if ans:
    print(ans)
else:
    print([-1])
