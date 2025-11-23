t = int(input())

times = [0] * t 
for i in range(t):

    x, y = map(int, input().split())
    if y == x:
        if x % 2 == 0:
            times[i] = 2 * x
        else:
            times[i] = (2 * x) - 1
    elif y == x - 2:
        if x % 2 == 0:
            times[i] = (2 * x) - 2
        else:
            times[i] = (2 * x) - 3
    else: 
        times[i] = -1
        
for i in range(t):
    print(times[i])