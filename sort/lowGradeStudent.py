from operator import itemgetter

n = int(input())

grades = []

for i in range(n):
    name, grade = input().split()
    grades.append([name, int(grade)])

# grades.sort(key = itemgetter(1))
grades.sort(key=lambda x:x[1])

for i in range(n):
    print(grades[i][0], end=' ')

