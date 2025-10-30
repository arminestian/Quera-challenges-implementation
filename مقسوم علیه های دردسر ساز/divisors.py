n = int(input())

mylist = []
counter = 0
sum = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
            mylist.append(j)

for i in mylist:
    sum += i
    
print(counter, sum)