n = int(input())

mydict = {}

for i in range(n):
    vurudi = list(input().split())
    if vurudi[0] in mydict:
        mydict[vurudi[0]] += 1
    else:
        mydict[vurudi[0]] = 1

maximum = 0

for i in mydict:
    if mydict[i] > maximum:
        maximum = mydict[i]
        
print(maximum)