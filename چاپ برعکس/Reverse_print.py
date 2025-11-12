mylist = []

while True:
    n = int(input())
    if n == 0:
        break
    mylist.append(n)
    
for i in range(len(mylist) - 1, -1, -1):
    print(mylist[i])