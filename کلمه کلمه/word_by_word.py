word = input()
c = 0

for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        c += 1
        
print(2 ** c)