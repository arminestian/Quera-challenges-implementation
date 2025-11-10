def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input())

i = 1
mylist = []

while fib(i) <= n:
    mylist.append(fib(i))
    i += 1
    
for i in range(1, n + 1):
    if i in mylist:
        print("+", end = "")
    else:
        print("-", end = "")