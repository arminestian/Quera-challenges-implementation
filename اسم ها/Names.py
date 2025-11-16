n = int(input())

counters = [[0] for i in range(n)]

for i in range(n):
    name = input()
    chars = []
    counter = 0
    for j in name:
        if j not in chars:
            chars.append(j)
            counter += 1
    counters[i] = counter
    
print(max(counters))    