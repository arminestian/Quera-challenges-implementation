import math
N, M, K = map(int, input().split())

milikavan = 2 ** K
milis = M * (2 ** M)
questions = {}
people = list()
for i in range(N):
    attendant = list(map(int, input().split()))
    for j in range(1, len(attendant)):
        if attendant[0] <= milikavan:
            if attendant[j] in questions:
                questions[attendant[j]] += 1
            else:
                questions[attendant[j]] = 1
    
    people.append(attendant)

if len(questions) == 0:
    question_score = 0
else:
    question_score = milis / len(questions)


for i in range(len(people)):

    rank = people[i][0]

    if rank > milikavan or len(people[i]) == 1:
        print(0)

    else:
        score = 0

        for j in range(1, len(people[i])):
            score += question_score / questions[people[i][j]]
        
        print(math.ceil(score))