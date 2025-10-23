n = int(input())
x = 0
y = 0

for i in range(1, n + 1):
    if i % 4 == 0:
        x = -i // 4
        y = i // 4
    elif i % 4 == 2:
        x = i // 4 + 1
        y = -(i // 4)
    elif i % 2 == 0:
        x = i // 3
        y = -(i // 4)
    elif i % 4 == 3:
        x = (i // 4) + 1
        y = (i // 4) + 1
    elif i % 4 == 1:
        x = -(i // 4)
        y = -(i // 4)
        
if n == 2:
    print("1 0")
else:
    print("%d %d" % (x, y))