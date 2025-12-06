a, b, c = map(float, input().split())

average = (a + b + c) / 3

if a == b == c:
    print(0)
elif (a == average) or (b == average) or (c == average):
    print(1)
else:
    print(2)