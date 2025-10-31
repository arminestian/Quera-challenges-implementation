m, n = map(int, input().split())
mylist = []
counter = 0

for i in range(m):
    mylist.append(list(map(int, input().split())))

for i in range(1, m - 1):
    for j in range(1, n - 1):
        if (mylist[i][j] > mylist[i][j + 1] and mylist[i][j] > mylist[i][j - 1] and mylist[i][j] < mylist[i - 1][j] and mylist[i][j] < mylist[i + 1][j]) or (mylist[i][j] < mylist[i][j + 1] and mylist[i][j] < mylist[i][j - 1] and mylist[i][j] > mylist[i - 1][j] and mylist[i][j] > mylist[i + 1][j]):
            counter += 1
            
print(counter)