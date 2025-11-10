n = int(input())
m = int(input())

if n == m:
    print(0)
elif (n == 1 and m != 4) or (n == 2 and m != 3) or (n == 3 and m != 2) or (n == 4 and m != 1):
    print(1)
else:
    print(2)