n, x, k = map(int, input().split())

shabake = []
for i in range(n):
    shabake.append(input())
if x + k > n:
    print(shabake[(x + k - 1) % n])
else:
    print(shabake[x + k - 1])