n = int(input())
s = list(map(int, input().split()))
maximum = 0
sum = 0
for i in s:
    sum += i
    if sum < 0:
        sum = 0
    if sum >= maximum:
        maximum = sum

print(maximum)