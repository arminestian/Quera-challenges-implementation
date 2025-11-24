n = int(input())

parts = int(0)
if (n % 2 == 0):
    parts = (n // 2 + 1) ** 2
else:
    parts = (n // 2 + 1) * (n // 2 + 2)
    
print(parts)