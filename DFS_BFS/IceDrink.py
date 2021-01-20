

def dfs(graph, i, j):
    print(f"x = {i}, y = {j}")

    graph[i][j] = 1

    x = [-1, 0, 1, 0]
    y = [0, 1, 0, -1]

    for a in range(len(x)):
        nowX = i+x[a]
        nowY = j+y[a]
        if nowX < 0 or nowX >= n or nowY < 0 or nowY >= m:
            continue
        if graph[nowX][nowY] == 0:
            dfs(graph, nowX, nowY)


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(f"count x, y = {i}, {j}")
            result += 1
            dfs(graph, i, j)

print(result)


"""
4 5
00110
00011
11111
00000
"""