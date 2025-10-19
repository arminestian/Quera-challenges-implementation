def tabdil_mabna(a, b, c):
    decimal = 0
    if b != 10:
        a_str = str(a)
        for i in range(len(a_str)):
            decimal += int(a_str[-(i+1)]) * (b ** i)
    else:
        decimal = a

    if decimal == 0:
        return "0"
    
    result = []
    while decimal > 0:
        result.append(int(decimal % c))
        decimal //= c
    
    return ''.join(str(x) for x in reversed(result))

def is_palindrome(n):
    return n == n[::-1]

a = int(input())
b = int(input())
c = int(input())

converted = tabdil_mabna(a, b, c)
if b == c and is_palindrome(str(a)):
    print("YES")
elif is_palindrome(converted):
    print("YES")
else:
    print("NO")
