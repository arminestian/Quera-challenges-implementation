n, m = map(int, input().split())

for i in range(3 * n):
    for j in range(3 * m):
        if (i < n or i >= 2 * n) and (j < m or j >= 2 * m):
            print("X", end="")
        elif (n <= i < 2 * n) and (m <= j < 2 * m):
            print("X", end="")
        else:
            print(".", end="")
    print()
