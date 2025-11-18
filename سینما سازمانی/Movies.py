n, k = map(int, input().split())

mylist = list(map(int, input().split()))
mylist.sort()
maximum = 0

for i in range(len(mylist)):
    if k > 0:
        if (k - (mylist[i] + 1)) >= 0:
            k -= (mylist[i] + 1)
            maximum += 1
            
print(maximum)