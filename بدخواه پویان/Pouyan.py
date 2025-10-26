p, d = map(int, input().split())

while True:
    if (p / 2) >= (d % p) >= 0:
        print(d)
        break
    else:
        d += d