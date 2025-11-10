p = list(map(int, input().split()))
x = int(input())

indice = p.index(x)
counter = 0

for i in range(indice, len(p)):
    counter += 1
    
if indice != 0:
    print(counter)
else:
    print(counter - 1)