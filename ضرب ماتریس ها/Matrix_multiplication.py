m ,n, p = map(int, input().split())
matrice1 = []
matrice2 = []
matrice3 = []
for i in range(m):
    row = list(map(int, input().split()))
    matrice1.append(row)
for i in range(n):
    row = list(map(int, input().split()))
    matrice2.append(row)

for i in range(m):
    for j in range(p):
        sum = 0
        for k in range(n):
            sum += matrice1[i][k] * matrice2[k][j]
        matrice3.append(sum)
k = 0
for i in range(m):
    for j in range(p):
        print(matrice3[k], end = " ")
        k += 1
    print()