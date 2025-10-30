t = int(input())
mylist = []

for i in range(t):

    counter = 0
    height = 0
    a, b, h = map(int, input().split())

    while True:

        if height + a >= h:
            counter += 1
            mylist.append(counter)
            break
        
        height += a - b
        counter += 1

for i in mylist:
    print(i)