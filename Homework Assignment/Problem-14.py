arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

n = len(arr)

if n <= 1:
    print(0)
elif arr[0] == 0:
    print(-1)
else:
    maxReach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        if i == n - 1:
            print(jumps)
            break

        maxReach = max(maxReach, i + arr[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            if i >= maxReach:
                print(-1)
                break
            steps = maxReach - i
