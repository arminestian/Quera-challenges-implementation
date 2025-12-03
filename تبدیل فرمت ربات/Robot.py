n = int(input())
s = input()

state = 0
string = str()
for i in range(n):
    match state:
        case 0:
            if s[i] == "R":
                string += "F"
            elif s[i] == "U":
                string += "RF"
                state = 1
            elif s[i] == "L":
                string += "RRF"
                state = 2
            else:
                string += "RRRF"
                state = 3

        case 1:
            if s[i] == "U":
                string += "F"
            elif s[i] == "L":
                string += "RF"
                state = 2
            elif s[i] == "D":
                string += "RRF"
                state = 3
            else:
                string += "RRRF"
                state = 0       

        case 2:
            if s[i] == "L":
                string += "F"
            elif s[i] == "D":
                string += "RF"
                state = 3
            elif s[i] == "R":
                string += "RRF"
                state = 0
            else:
                string += "RRRF"
                state = 1         

        case 3:
            if s[i] == "D":
                string += "F"
            elif s[i] == "R":
                string += "RF"
                state = 0
            elif s[i] == "U":
                string += "RRF"
                state = 1
            else:
                string += "RRRF"
                state = 2

print(string)