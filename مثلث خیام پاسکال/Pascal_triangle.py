n = int(input())

mylist = [[1] * (i + 1) for i in range(n)]

for i in range(2, n):
    for j in range(1, len(mylist[i - 1])):
        mylist[i][j] = mylist[i - 1][j - 1] + mylist[i - 1][j]
        
for i in mylist:
    for j in i:
        print(j, end = " ")
    print()