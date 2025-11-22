t = int(input())

for i in range(t):
    n = int(input())
    ans = 0
    x = 1
    while x * x < n:
        if n % x == 0 and (x + n // x) % 2 == 0:
            ans += 1
        x += 1
    print(ans)