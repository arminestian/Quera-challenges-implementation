t = int(input())

answers = list()

for i in range(t):
    color = input()
    answer = "#"
    for j in range(1,len(color)):
        if color[j] == "0":
            answer += "F"
        elif color[j] == "1":
            answer += "E"
        elif color[j] == "2":
            answer += "D"
        elif color[j] == "3":
            answer += "C"
        elif color[j] == "4":
            answer += "B"
        elif color[j] == "5":
            answer += "A"
        elif color[j] == "6":
            answer += "9"
        elif color[j] == "7":
            answer += "8"
        elif color[j] == "8":
            answer += "7"
        elif color[j] == "9":
            answer += "6"
        elif color[j] == "A":
            answer += "5"
        elif color[j] == "B":
            answer += "4"
        elif color[j] == "C":
            answer += "3"
        elif color[j] == "D":
            answer += "2"
        elif color[j] == "E":
            answer += "1"
        elif color[j] == "F":
            answer += "0"
    answers.append(answer)

for i in answers:
    print(i)
    