def solution(n, lost, reserve):
    answer = 0

    students = [0 for i in range(n+1)]

    for i in lost:
        students[i] -= 1

    for i in reserve:
        students[i] += 2

    # print(students)

    for i in range(1, n+1):
        if students[i] < 0:
            front = i-1
            back = i+1

            if front > 0:
                if students[front] > 1:
                    students[front] -= 1
                    students[i] += 1

            if students[i] < 0:
                if back <= n:
                    if students[back] > 1:
                        students[back] -= 1
                        students[i] += 1
    # print(students)

    for i in range(1, n+1):
        if students[i] >= 0:
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))