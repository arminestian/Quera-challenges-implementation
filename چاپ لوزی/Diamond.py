n = int(input())
for i in range((2 * n) + 1):
    if i <= n:
        print(((n - i) * " ") + (((2 * i) + 1) * "*") + ((n - i) * " "))
    else:
        print(((i - n) * " ") + (((((2 * n) - i) * 2) + 1) * "*") + ((i - n) * " "))