a, b, l = map(int, input().split())

timer = 0
timer += a
l -= 1

if l == 0:
    print(timer)
else:
    for i in range(l):
        if i % 2 == 0:
            timer += b
        else:
            timer += a
    print(timer)