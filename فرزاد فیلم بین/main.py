n = int(input())
answers = []
for i in range(n):
    film = input()
    answer = ""
    for j in range(len(film)):
        if j == 0 or film[j - 1] == " ":
            answer += film[j].upper()
        else:
            answer += film[j].lower()
    answers.append(answer)
for i in range(n):
    print(answers[i])