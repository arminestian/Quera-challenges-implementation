a = int(input())
b = int(input())
for i in range(1, a + 1):
    if b >= a:
        print("Wrong order!")
        break
    elif ((a - b) % 2) != 0:
        print("Wrong difference!")
        break
    for j in range(1, a + 1):
        if (((a - b) // 2) < j < a - ((a - b) // 2) + 1) and (((a - b) // 2) < i < a - ((a - b) // 2) + 1):
            print(" ", end = " ")
        else:
            print("*", end = " ")
    print()