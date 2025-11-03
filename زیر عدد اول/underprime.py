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

n = int(input())

mylist = ["1", "2", "3", "5", "7", "9"]
mylist2 = mylist.copy()
mylist2.pop(0)
mylist2.pop()

superprime = 0
flag = False

while superprime == 0:
        if n == 1:
            superprime = 2
            break
        elif n == 2:
            superprime = 3
            break
        elif n == 3:
            superprime = 5
            break
        elif n == 4:
            superprime = 7
            break
        else:
            for i in mylist2:
                if flag == True:
                    break
                for j in mylist:
                    if is_prime(int(i + j)):
                        mylist2.append(str(int(i + j)))
                        if len(mylist2) == n:
                            superprime = mylist2[-1]
                            flag = True
                            break
                        
print(superprime)