n = input()
flag = True
j = 1
for i in n:
    if i != n[len(n) - j]:
        flag = False
        break
    j += 1
if flag == True:
    print("Yes")
else:
    print("No")