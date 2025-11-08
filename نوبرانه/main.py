a = list(map(int, input().split()))

counter = 0

for i in range(len(a)):
    if a[i] >= 80:
        counter += 1
        
if counter >= 3:
    print("Mamma mia!")
elif counter == 1 or counter == 2:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")