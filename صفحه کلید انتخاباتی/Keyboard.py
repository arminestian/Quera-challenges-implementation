n = int(input())

capslock = False
answer = []

for i in range(n):
    vurudi = input()
    if vurudi == "CAPS":
        if capslock == True:
            capslock = False
        else:
            capslock = True
    else:
        if capslock == True:
            answer.append(vurudi.upper())
        else:
            answer.append(vurudi.lower())
            
for i in answer:
    print(i, end = "")