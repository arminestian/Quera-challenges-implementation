n, a, b, c ,d = map(int, input().split())
counter = 0
for i in range(1, n + 1):
    if i % a == 0:
        counter += 1
        continue
    elif i % b == 0:
        counter += 1
        continue
    elif i % c == 0:
        counter += 1
        continue
    elif i % d == 0:
        counter += 1
        continue
print(counter)