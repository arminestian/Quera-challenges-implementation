n = int(input())

mylist = ["a", "b"]
for i in range(n):
    mylist.append(mylist[i] + "a")
    mylist.append(mylist[i] + "b")
    
print(mylist[n + 1][-1])