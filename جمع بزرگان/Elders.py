a = input()
operator = input()
b = input()

if operator == "*":
    answer = a + (b.count("0") * "0")
elif operator == "+":
    answer = str(int(a) + int(b))
    
print(answer)