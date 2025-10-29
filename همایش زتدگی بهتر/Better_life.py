r, c = map(int, input().split())
radif = 10 - (r - 1)
sandali = 0
jahat = ""

if c > 10:
    sandali = c - 10 + 1
    jahat = "Left"
else:
    sandali = 11 - c
    jahat = "Right"
    
print(jahat, str(radif), str(sandali), sep = " ")