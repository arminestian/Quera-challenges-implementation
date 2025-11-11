n = int(input())
string = input()

flag = True
for i in range(n):
    if (string[i] + string[i + n]) != "FS" and (string[i] + string[i + n]) != "SF":
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")