n = int(input())

students = []

for i in range(n):
    data = list(map(str, input().split()))
    students.append([data[0], int(data[1]), int(data[2]), int(data[3])])

students.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(students[i][0])
