s = input()

K = s.count("T")
G = s.count("D")
R1 = s.count("L")
R2 = s.count("F")

total = K + G + R1 + R2

print(2 ** total)