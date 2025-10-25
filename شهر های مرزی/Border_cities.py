n = int(input())
m = int(input())

if n == 1:
    print(m)
elif m == 1:
    print(n)
else:
    print(2 * (m - 1 + n - 1))