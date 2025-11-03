s = input()

flag = False
i = 0

while i < len(s):
    counter = 0
    k = s[i]
    j = i
    
    while True:
        if j < len(s):
            if s[j] == s[i]:
                counter += 1
                j += 1
            else:
                break
        else:
            break

    if counter % 2 != 0:
        flag = True
        break

    i += counter

if flag:
    print("bad")
else:
    print("khoob")