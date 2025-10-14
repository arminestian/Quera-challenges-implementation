import math
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())
primes = []
for i in range(a, b + 1):
    if is_prime(i):
        primes.append(i)
for i in primes:
    print(i)