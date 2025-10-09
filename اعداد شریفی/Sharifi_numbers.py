n = int(input())
mylist = []
sharifi = []
sum = 0
for i in range(n):
    number = int(input())
    mylist.append(number)
for i in range(n):
    for j in range(i + 1, n):
        sum += mylist[i] * mylist[j]
sum *= 2
for i in range(100, sum + 1):
    length = len(str(i))
    num = str(i)
    sumnumber = 0
    for j in range(length):
        sumnumber += int(num[j]) ** length
    if sumnumber == i:
        sharifi.append(i)
for i in sharifi:
    print(i)