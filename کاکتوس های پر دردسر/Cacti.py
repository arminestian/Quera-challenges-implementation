n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] <= 3:
        print(a[i] * "*")
    else:
        print("*")