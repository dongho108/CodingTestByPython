from collections import deque

def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
    print("=====")


n = int(input())
graph = []

max_height = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if max_height < graph[i][j]:
            max_height = graph[i][j]

safety_list = []

for rain in range(0, max_height+1):
    visited = [[False]*n for _ in range(n)]
    safety = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] < rain or visited[i][j]:
                continue
            safety += 1

            q = deque()
            q.append((i,j))
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for d in dir:
                    nx = x + d[0]
                    ny = y + d[1]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] < rain or visited[nx][ny]:
                        continue

                    q.append((nx, ny))
                    visited[nx][ny] = True

    safety_list.append(safety)

print(max(safety_list))

'''
7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9
'''