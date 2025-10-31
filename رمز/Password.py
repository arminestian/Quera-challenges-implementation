k = int(input())
password = input()
mylist = []

for i in range(k):
    mylist.append(input())

counter = 0

for i in range(len(password)):
    for j in mylist[i]:
        if j == password[i]:
            indice = mylist[i].index(str(password[i]))
            if indice > 4:
                counter += 9 - indice
                break
            else:
                counter += indice
                break
            
print(counter) 