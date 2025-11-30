def is_subsequence(s, t):
    i = 0 
    j = 0 

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s)


t = int(input())
ans = list()
for i in range(t):
    s = input()
    if is_subsequence("acpc", s) and len(s) > 4:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)
    