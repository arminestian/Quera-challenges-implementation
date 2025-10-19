import math
n = int(input())

def func(n):
    if n % 2 == 1:
        return None
    
    i = int(math.sqrt(n))
    j = n // 2
    k = n - j - i
    
    while (pow(i, 2) + pow(j, 2) != pow(k, 2)):
        if (pow(i, 2) + pow(j, 2)) > pow(k, 2):
            j -= 1
        elif (pow(i, 2) + pow(j, 2)) < pow(k, 2):
            i += 1
        if i > j:
            return None
        
        k = n - j - i

    if (pow(i, 2) + pow(j, 2) != pow(k, 2)):
        return None
    return i, j, k
        
result = func(n)
if result == None:
    print("Impossible")
else:
    print(*result)