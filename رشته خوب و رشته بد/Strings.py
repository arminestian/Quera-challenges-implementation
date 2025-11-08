s = input()
t = input()
n = int(input())

if t in s or len(s) > n:
    print(-1)
else:
    x = str()
    for i in range(n - len(s)):
        x += "x"
    x += s
    print(x)