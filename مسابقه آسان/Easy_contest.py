def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n, k = map(int, input().split())
mynumber = str(fact(n))
print(mynumber.count(str(k)))