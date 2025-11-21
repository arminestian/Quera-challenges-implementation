n, k = map(int, input().split())

if n // k >= 2:
    print(0)
else:
    print(n -( ((n - k) * 2) + 1))