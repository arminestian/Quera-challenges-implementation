a = int(input())
b = int(input())

if (a % 10) > (b % 10):
    print("%d < %d" % (b, a))
elif (a % 10) < (b % 10):
    print("%d < %d" % (a, b))
else:
    if ((a % 100) // 10) > ((b % 100) // 10):
        print("%d < %d" % (b, a))
    elif ((a % 100) // 10) < ((b % 100) // 10):
        print("%d < %d" % (a, b))
    else:
        if a > b:
            print("%d < %d" % (b, a))
        elif a < b:
            print("%d < %d" % (a, b))
        else:
            print ("%d = %d" % (a, b))