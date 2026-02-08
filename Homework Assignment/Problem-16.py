a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]

n = len(a)
m = len(b)

gap = (n + m + 1) // 2

while gap > 0:
    i = 0
    j = gap

    while j < n + m:
        if i < n and j < n:
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
        elif i < n and j >= n:
            if a[i] > b[j - n]:
                a[i], b[j - n] = b[j - n], a[i]
        else:
            if b[i - n] > b[j - n]:
                b[i - n], b[j - n] = b[j - n], b[i - n]
        i += 1
        j += 1

    if gap == 1:
        gap = 0
    else:
        gap = (gap + 1) // 2

print("a[] =", a)
print("b[] =", b)
