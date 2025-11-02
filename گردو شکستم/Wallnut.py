n, x, y = map(int, input().split())
flag = False

if n % x == 0 and n % y != 0:
    print(n // x, 0)

elif n % x != 0 and n % y == 0:
    print(0, n // y)

else:
    counterx = 0
    countery = 0

    while n > 0:
        if n >= x:
            n -= x
            counterx += 1

            if n % y == 0:
                countery = n // y
                n = 0
                
        elif n >= y:
            n -= y
            countery += 1

            if n % x == 0:
                counterx = n // y
                n = 0

        elif n != 0:
            print(-1)
            flag = True
            break
        
    if flag == False:
        print(counterx, countery) 