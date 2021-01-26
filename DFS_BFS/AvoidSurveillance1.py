from itertools import combinations


def surceillance(tchs, tList):
    # 선생님 3명 상하좌우 쭉 감시

    for teacher in tchs:
        x, y = teacher[0], teacher[1]
        # 상
        for i in range(x-1, -1, -1):
            if tList[i][y] == "O":
                break
            elif tList[i][y] == "S":
                return False

        # 우
        for i in range(y+1, n):
            if tList[x][i] == "O":
                break
            elif tList[x][i] == "S":
                return False

        # 하
        for i in range(x+1, n):
            if tList[i][y] == "O":
                break
            elif tList[i][y] == "S":
                return False

        # 좌
        for i in range(y-1, -1, -1):
            if tList[x][i] == "O":
                break
            elif tList[x][i] == "S":
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
    for i in range(3):
        x = o[i][0]
        y = o[i][1]
        school[x][y] = "O"

    if surceillance(teachers, school):
        answer = "YES"
        break

    for i in range(3):
        x = o[i][0]
        y = o[i][1]
        school[x][y] = "X"


print(answer)



