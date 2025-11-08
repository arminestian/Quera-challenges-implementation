def magsumalieyh(n, x):
    mylist = []
    for i in range(1, x):
        if n % i == 0:
            mylist.append(i)
    return mylist

a, b, x = map(int, input().split())
list1 = magsumalieyh(a, x)
list2 = magsumalieyh(b, x)

counter = 0
for i in list1:
    for j in list2:
        if i + j <= x:
            counter += 1

print(counter)