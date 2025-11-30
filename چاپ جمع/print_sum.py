n = int(input())

sum = 0
for i in range(1, n + 1):
    sum += i
    if i != n:
        print(str(i) + " + ", end="")
    else:
        print(str(i) + " = " + str(sum))
