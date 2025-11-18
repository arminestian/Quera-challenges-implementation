t = int(input())

for i in range(t):
    n = int(input())
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    print(2 ** k)