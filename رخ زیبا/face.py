x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

if ((x1 == x3 or y1 == y3 or x1 == x4 or y1 == y4) and not((x2 == x3) or (y2 == y3) or (x2 == x4) or (y2 == y4))) or ((x2 == x3 or y2 == y3 or x2 == x4 or y2 == y4) and not((x1 == x3) or (x1 == x4) or (y1 == y3) or (y1 == y4))):
    print("happy")
else:
    print("unhappy")