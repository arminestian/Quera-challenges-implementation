s = list(input())

for i in range(1, len(s) + 1):
    for k in s:
        print(k, end = "")
    if i == len(s):
        break
    for j in range(i):
        s[j] = s[i]    
    print()    