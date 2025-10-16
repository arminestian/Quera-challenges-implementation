n = input()
r1 = input()
r2 = input()

c = 0
l = len(r1)
for i in range(l):
    if r1[i] != r2[i]:
        c += 1

if c % 2 == 0:
    print(int(c / 2))
else:
    print("NO")