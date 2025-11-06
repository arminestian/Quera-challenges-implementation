mylist = [[] for i in range(4)]

for i in range(4):
    k = list(map(int, input().split()))
    for j in range(len(k)):
        mylist[i].append(k[j])

maximums = []
for i in range(4):
    maximums.append(max(mylist[i]))

maximum = max(maximums)

for i in range(4):
    if maximum in mylist[i]:
        print(i + 1)
        break