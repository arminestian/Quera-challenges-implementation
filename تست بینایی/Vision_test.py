n = int(input())
s = input()
p = input()

counter = 0

for i in range(n):
    if s[i] != p[i]:
        counter += 1
        
print(counter)