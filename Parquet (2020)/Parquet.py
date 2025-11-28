def find_dimensions(black, yellow):
    for W in range(3, 10000):
        for L in range(3, 10000):
            if (W - 2) * (L - 2) == yellow and (2 * (W + L) - 4) == black:
                return W, L

black , yellow= map(int, input().split())
W, L = find_dimensions(black, yellow)
print(L, W)
