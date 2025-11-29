h = int(input())
k = int(input())

if ((h * 2) + k) % 2 == 0:
    if k == 0 and h % 2 == 1:
        print("NO")
    else:
        print("YES")
else:
    print("NO")