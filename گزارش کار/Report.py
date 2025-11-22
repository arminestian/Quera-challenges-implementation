n, k = map(int, input().split())

sum = 0

for i in range(n):
    sum += int(input())
if sum >= k:
    print("YES")
else:
    print("NO")