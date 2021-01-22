def display(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=' ')
        print()
    print("----")

def dfs(graph, start, s):
    if s == 0:
        return

    # display(graph)

    # 방문처리
    for i in range(len(start)-1, -1, -1):
        for j in range(len(start[i])):
            nx = start[i][j][0]
            ny = start[i][j][1]
            graph[nx][ny] = i
    # display(graph)
    # 상 하 좌 우
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    newstart = [[] for i in range(k+1)]

    for i in range(len(start)):
        for j in range(len(start[i])):
            for d in dir:
                # print(i, j)
                # print(start[i][j])
                nowx = start[i][j][0] + d[0]
                nowy = start[i][j][1] + d[1]

                if nowx < 0 or nowx >= n or nowy < 0 or nowy >= n:
                    continue
                if graph[nowx][nowy] == 0:
                    newstart[i].append([nowx, nowy])
    dfs(graph, newstart, s-1)

n, k = map(int, input().split())

graph = [[0]*n for i in range(n)]
newstart = [[] for i in range(k+1)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if 0 < graph[i][j] <= k:
            newstart[graph[i][j]].append((i, j))
s, x, y = map(int, input().split())
# print(graph)
# print(newstart)


for time in range(s):

    # display(graph)
    start = [[] for i in range(k+1)]

    for i in range(len(newstart)):
        for j in range(len(newstart[i])):
            start[i].append((newstart[i][j][0], newstart[i][j][1]))

    newstart = [[] for i in range(k + 1)]
    # 방문처리
    for i in range(len(start) - 1, -1, -1):
        for j in range(len(start[i])):
            nx = start[i][j][0]
            ny = start[i][j][1]
            graph[nx][ny] = i
    # display(graph)
    # 상 하 좌 우
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


    for i in range(len(start)):
        for j in range(len(start[i])):
            for d in dir:
                # print(i, j)
                # print(start[i][j])
                nowx = start[i][j][0] + d[0]
                nowy = start[i][j][1] + d[1]

                if nowx < 0 or nowx >= n or nowy < 0 or nowy >= n:
                    continue
                if graph[nowx][nowy] == 0:
                    newstart[i].append([nowx, nowy])

print(graph[x-1][y-1])