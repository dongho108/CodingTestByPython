n = int(input())
quizs = []
for i in range(n):
    quizs.append(list(input()))

answer = []
for quiz in quizs:
    score = 0
    continue_score = 1
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            score += continue_score
            continue_score += 1
        else:
            continue_score = 1
    answer.append(score)

for i in range(n):
    print(answer[i])