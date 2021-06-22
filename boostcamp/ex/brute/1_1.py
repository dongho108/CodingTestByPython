def solution(answers):
    answer = []

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            score[0] += 1
        if answers[i] == b[i % len(b)]:
            score[1] += 1
        if answers[i] == c[i % len(c)]:
            score[2] += 1

    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))