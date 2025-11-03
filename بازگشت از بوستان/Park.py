x, y = map(int, input().split())
x1, y1 = map(int, input().split())

if x - x1 >= 0:
    print("Left")
else:
    print("Right")
