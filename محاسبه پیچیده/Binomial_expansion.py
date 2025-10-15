def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

a, x, n = map(int, input().split())
sum = 0
for k in range(n + 1):
    sum += (fact(n) // (fact(k) * fact(n - k))) * (x ** k) * (a ** (n - k))
print(sum)