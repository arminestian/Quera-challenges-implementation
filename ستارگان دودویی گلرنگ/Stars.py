n = int(input())
s = input()

def print_s(s):
    for line in range(3):
        for i in range(len(s)):
            if line == 0:   
                if s[i] == "1":
                    print(".*.", end="")
                else:
                    print("***", end="")
            elif line == 1:
                if s[i] == "1":
                    print(".*.", end="")
                else:
                    print("*.*", end="")
            else:
                if s[i] == "1":
                    print(".*.", end="")
                else:
                    print("***", end="")
                    
        print()
print_s(s)