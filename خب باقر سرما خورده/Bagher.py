mylist = []
answers = []

for i in range(5):
    string = input()
    mylist.append(string)

for i in range(len(mylist)):
    if "HAFEZ" in mylist[i] or "MOLANA" in mylist[i]:
        answers.append(i + 1)
        
if len(answers) == 0:
    print("NOT FOUND!")
else:
    for i in answers:
        print(i, end = " ")