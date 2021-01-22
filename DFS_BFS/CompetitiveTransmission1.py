from collections import deque


def display(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=' ')
        print()
    print("----")


n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append((list(map(int, input().split()))))
    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j], i, j, 0])
target_s, target_x, target_y = map(int, input().split())

data.sort()
queue = deque(data)

# 상 하 좌 우
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while queue:
    virus, x, y, s = queue.popleft()
    if s == target_s:
        break
    for d in dir:
        nowX = x + d[0]
        nowY = y + d[1]
        if nowX < 0 or nowY < 0 or nowX >= n or nowY >= n:
            continue
        if graph[nowX][nowY] == 0:
            queue.append([virus, nowX, nowY, s+1])
            graph[nowX][nowY] = virus

# display(graph)
print(graph[target_x-1][target_y-1])

