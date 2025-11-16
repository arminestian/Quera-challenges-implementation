n, m = map(int,input().split())

costs = []
sum = 0

for i in range(n):
    costs.append(list(map(int,input().split())))

for i in range(m):
    travel = list(map(int, input().split()))
    sum += costs[travel[0] - 1][travel[1] - 1]
    
print(sum)