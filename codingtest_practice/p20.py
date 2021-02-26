from itertools import combinations


def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
    print("=====")


n = int(input())
graph = []
teacher = []
blank = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        elif graph[i][j] == 'X':
            blank.append((i,j))

obj = list(combinations(blank, 3))
temp_graph = [['A'] * n for _ in range(n)]


def watch(t, temp_graph):
    # 선생님 한명이 모든방향에 대해 학생 찾기
    # 학생 발견하면 False return
    x, y = t[0], t[1]

    # 상
    for i in range(x-1, -1, -1):
        if temp_graph[i][y] == "O":
            break
        elif temp_graph[i][y] == "S":
            return False

    # 하
    for i in range(x+1, n):
        if temp_graph[i][y] == "O":
            break
        elif temp_graph[i][y] == "S":
            return False

    # 좌
    for i in range(y-1, -1, -1):
        if temp_graph[x][i] == "O":
            break
        elif temp_graph[x][i] == "S":
            return False

    # 우
    for i in range(y+1, n):
        if temp_graph[x][i] == "O":
            break
        elif temp_graph[x][i] == "S":
            return False

    return True


def surveillance(graph):
    # 상 하 좌 우

    answer = False
    for ob in obj:
        for o in ob:
            graph[o[0]][o[1]] = 'O'

        for a in range(n):
            for b in range(n):
                temp_graph[a][b] = graph[a][b]
        check = True
        for t in teacher:
            # 감시 피하면 True return
            if not watch(t, temp_graph):
                check = False
                break

        if check == True:
            return True

        for o in ob:
            graph[o[0]][o[1]] = 'X'
    return answer


if surveillance(graph):
    print("YES")
else:
    print("NO")