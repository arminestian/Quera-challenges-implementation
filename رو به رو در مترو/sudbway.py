row1 = list(input().split())
row2 = list(input().split())

counter = 0
for i in range(len(row1)):
    if row1[i] == row2[i] == '1':
        counter += 1
        
print(counter)