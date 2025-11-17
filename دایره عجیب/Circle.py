n, k = map(int , input().split())

turn = 1
flag = False
counter = 0

while turn != 1 or flag == False:
    if turn > n:
        turn %= n
        if turn == 1:
            flag = True
    if turn == 1 and flag == True:
        break
    turn += k
    counter += 1
    
print(counter)    