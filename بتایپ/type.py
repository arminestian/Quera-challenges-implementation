S = list(input())

j = 0
while True:
    if S[j] == "=":
        if j == 0:
            S.pop(0)
            continue
        else:
            S.pop(j - 1)
            S.pop(j - 1)
            j -= 2
    if j == len(S) - 1:
        break
    j += 1
    
for i in S:
    print(i, end = "")