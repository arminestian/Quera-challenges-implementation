n = int(input())
k = int(input())
s = list(input())
for i in range(k):
    s.insert(0, s[-1])
    s.pop(len(s) - 1)
    for j in range(len(s)):
        if s[j] == "z":
            s[j] = "a"
        else:
            s[j] = chr((ord(s[j]) + 1))
ans = ""
for i in s:
    ans += i
print(ans)