def same_score(x, students, student_score, n):
    visited = [False for _ in range(n)]

    student_student = [[False] * n for _ in range(n)]

    for i in range(n):
        visited[i] = True
        target = students[i][x]
        same_count = 0
        now_visited = [i]
        for j in range(i+1, n):
            if not visited[j]:
                if students[j][x] == target:
                    same_count += 1
                    visited[j] = True
                    now_visited.append(j)
        for j in now_visited:
            
            student_score[j] += same_count


n = int(input())
students = []

for i in range(n):
    students.append(list(map(int, input().split(" "))))


student_score = [0 for _ in range(n)]


for i in range(5):
    same_score(i, students, student_score, n)

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