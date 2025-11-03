t = int(input())

mylist = []

for i in range(t):

    n = int(input())
    score = input()
    c = 0
    q = 0

    for j in score:
        if j == "Q":
            q += 1
        elif j == "C":
            c += 1

    if c > q:
        mylist.append("CodeCup")
    elif q > c:
        mylist.append("Quera")
        
for i in mylist:
    print(i)