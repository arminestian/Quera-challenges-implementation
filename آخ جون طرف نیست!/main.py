mylist = []

for i in range(3):

    n = int(input())
    days = input().split()
    for i in range(n):

        if days[i] not in mylist:
            mylist.append(days[i])
            
print(7 - len(mylist))  