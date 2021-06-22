n = int(input())
students = []

for i in range(n):
    students.append(list(map(int, input().split(" "))))

student_student = [[False] * n for _ in range(n)]
# print(student_student)

for k in range(5):
    for i in range(n):
        for j in range(i + 1, n):
            if students[i][k] == students[j][k]:
                student_student[i][j] = True
                student_student[j][i] = True

student_score = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if student_student[i][j]:
            student_score[i] += 1


# print(student_score)
max_value = max(student_score)
for i in range(n):
    if student_score[i] == max_value:
        print(i+1)
        break



# 7
# 2 3 1 7 3
# 4 1 9 6 8
# 5 5 2 4 4
# 6 5 2 6 7
# 8 4 2 2 2
# 2 3 1 7 3
# 2 3 1 7 3


# 3
# 2 3 1 7 3
# 4 1 9 6 8
# 5 5 2 4 4