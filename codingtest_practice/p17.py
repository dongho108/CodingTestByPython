from collections import deque

n, k = map(int, input().split())

graph = []
start = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            start.append((graph[i][j], i, j, 0))

s, rx, ry = map(int, input().split())

start.sort()
q = deque(start)

while q:
    virus, x, y, time = q.popleft()

    if time == s:
        break

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in dir:
        nx = d[0] + x
        ny = d[1] + y

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            q.append((virus, nx, ny, time+1))
            graph[nx][ny] = virus

print(graph[rx-1][ry-1])