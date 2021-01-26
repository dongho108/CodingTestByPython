from itertools import combinations


def initList(original):
    re = [[0]*len(original) for i in range(len(original))]

    for i in range(len(original)):
        for j in range(len(original)):
            re[i][j] = original[i][j]

    return re


def surceillance(tchs, tList):
    # 선생님 3명 상하좌우 쭉 감시

    for teacher in teachers:
        x, y = teacher[0], teacher[1]
        # 상
        for i in range(x-1, -1, -1):
            if tempList[i][y] == "O":
                break
            elif tempList[i][y] == "S":
                return False

        # 우
        for i in range(y+1, n):
            if tempList[x][i] == "O":
                break
            elif tempList[x][i] == "S":
                return False

        # 하
        for i in range(x+1, n):
            if tempList[i][y] == "O":
                break
            elif tempList[i][y] == "S":
                return False

        # 좌
        for i in range(y-1, -1, -1):
            if tempList[x][i] == "O":
                break
            elif tempList[x][i] == "S":
                return False
    return True


n = int(input())
school = []
students = []
teachers = []
blanks = []
for i in range(n):
    school.append(list(map(str, input().split())))
    for j in range(n):
        if school[i][j] == "S":
            students.append([i, j])
        elif school[i][j] == "T":
            teachers.append(([i, j]))
        else:
            blanks.append([i, j])

objects = list(combinations(blanks, 3))
answer = "NO"

for o in objects:
    tempList = initList(school)
    for i in range(3):
        x = o[i][0]
        y = o[i][1]
        tempList[x][y] = "O"

    if surceillance(teachers, tempList):
        answer = "YES"
        break

print(answer)



