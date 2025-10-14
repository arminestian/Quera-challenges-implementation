import math
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1):
             if n % i == 0:
                 return False
        return True
    
a = int(input())
b = int(input())
answers = []
for i in range(a + 1, b):
    if is_prime(i):
        answers.append(i)
        answers.append(",")
if len(answers) != 0:
    answers.pop(-1)
for i in answers:
    print(i, end = "")