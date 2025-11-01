X = int(input())
N = int(input())

if N == 0:
    print(20)
elif N == 7:
    print(X)
else:
    score = X - N
    if score < 0:
        print(0)
    else:
        print(score)    