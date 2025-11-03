n, m = map(int, input().split())
counter = [0, 0]

for i in range(2 * n):
    vurudi = list(input())
    for j in vurudi:
        if i < n:
            if j == "*":
                counter[0] += 1
        else:
            if j == "*":
                counter[1] += 1
                
print(counter[0], counter[1])