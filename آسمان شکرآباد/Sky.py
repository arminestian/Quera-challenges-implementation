n, m = map(int, input().split())

counter = 0

for i in range(n):
    s = input()
    for j in s:
        if j == "*":
            counter += 1
            
print(counter)