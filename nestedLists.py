student_list = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student_list.append([name, score])
    scores.append(score)
secondMinimumScore = min(x for x in scores if x!=min(scores))
namesList = []
for i in student_list:
    if i[1] == secondMinimumScore:
        namesList.append(i[0])
namesList = sorted(namesList)
print('\n'.join(namesList))