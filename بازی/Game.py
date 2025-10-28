n = int(input())
numbers = list(map(int, input().split()))
array = []

for i in range(len(numbers)):
    if i % 2 == 0:
        array.append(max(numbers))
        numbers.remove(max(numbers))
    else:
        array.append(min(numbers))
        numbers.remove(min(numbers))
        
for i in array:
    print(i, end = " ")