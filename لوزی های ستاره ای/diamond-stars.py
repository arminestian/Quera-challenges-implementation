n = int(input())
c = int(n / 2)
for i in range(n):
    if(i < n / 2):
        print(c * " " + (((i + 1) * 2) - 1) * "*" + (2*c) * " " + (((i + 1) * 2) - 1) * "*")
        if (c > 0):
            c -= 1
    else:
        c += 1
        print(c * " " + (((n - i) * 2) - 1) * "*" + (2*c) * " " + (((n - i) * 2) - 1) * "*")