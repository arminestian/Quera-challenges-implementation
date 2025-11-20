k = int(input())
n = int(input())
a = list(map(int, input().split()))

time = 0
time += n

a.append(0)
height = 0

for i in range(len(a)):
    if abs(height - a[i]) % k == 0:
        time += abs(height - a[i]) // k
    else:
        time += (abs(height - a[i]) // k) + 1
    height = a[i]
    
print(time)