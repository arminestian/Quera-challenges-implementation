n = int(input())

columns = []
for i in range(n):
    columns.append(int(input()))
    
height = sum(i for i in columns) // n
counter = 0

for i in range(n):
    if columns[i] < height:
        counter += height - columns[i]
        
print(counter)