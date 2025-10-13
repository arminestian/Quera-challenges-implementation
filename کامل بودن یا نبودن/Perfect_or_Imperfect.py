def kamel(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False
n = int(input())

if kamel(n):
    print("YES")
else:
    print("NO")
            