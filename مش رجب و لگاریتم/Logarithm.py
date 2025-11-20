n = int(input())

counter = 0

while n > 0:
    n //= 2
    counter += 1
print(counter - 1)