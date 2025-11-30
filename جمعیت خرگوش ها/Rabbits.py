P, L = map(int, input().split())
Y = int(input())

for i in range(Y):
    P = (P * 2) - L
    
print(P)
