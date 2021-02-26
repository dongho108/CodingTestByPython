from itertools import combinations

def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
    print("====")


def dfs(start, arr):
    x = start[0]
    y = start[1]
    arr[x][y] = 2

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if arr[nx][ny] == 0:
            dfs((nx, ny), arr)


def count_blank(gr):
    count = 0
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            if gr[i][j] == 0:
                count += 1
    return count


n, m = map(int, input().split())

graph = []
temp_graph = [[0] * m for _ in range(n)]
virus = []
blank = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            blank.append((i, j))

pre_blank = list(combinations(blank, 3))


max_value = 0
for pb in pre_blank:
    for b in pb:
        graph[b[0]][b[1]] = 1
    for i in range(n):
        for j in range(m):
            temp_graph[i][j] = graph[i][j]
    # display(temp_graph)
    for v in virus:
        dfs(v, temp_graph)
    # display(temp_graph)
    blank_num = count_blank(temp_graph)
    # print(blank_num)
    if max_value < blank_num:
        max_value = blank_num
    for b in pb:
        graph[b[0]][b[1]] = 0

print(max_value)