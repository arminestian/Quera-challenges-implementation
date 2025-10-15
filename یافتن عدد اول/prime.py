def sumdigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def number_prime(n, x):
    counter = 0
    prime = 0
    while counter < x:
        if is_prime(n + 1):
            prime = n + 1
            counter += 1
        n += 1
    return prime

n = int(input())
print(number_prime(n, sumdigit(n)))