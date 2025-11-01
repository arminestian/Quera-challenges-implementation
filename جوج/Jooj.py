n = int(input())
numbers = list(map(int, input().split()))
flag = False

for i in range(1, n - 1):
    if numbers[i - 1] < numbers[i] > numbers[ i + 1]:
        flag = True
        
if flag:
    print("Ey baba :(")
else:
    print("Bah Bah! Ajab jooji!")