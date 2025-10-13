a, b = map(int, input().split())
maximum = max(a, b)
for i in range(2, maximum):
    if abs(b - a) % i == 0:
        print(str(i), end = " ")