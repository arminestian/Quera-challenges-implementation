a, b, c = map(int, input().split())

if (0 < a < 180) and (0 < b < 180) and (0 < c < 180) and (a + b + c == 180):
    print("Yes")
else:
    print("No")