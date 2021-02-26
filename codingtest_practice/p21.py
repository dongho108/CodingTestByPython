from collections import deque


def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
    print("=====")


n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

count = 0
count_noU = 0
while count_noU < (n*n):
    print('==============')
    union_list = []
    temp_graph = [[0]*n for _ in range(n)]

    color = 0
    for i in range(n):
        for j in range(n):
            if temp_graph[i][j] != 0:
                continue
            color += 1
            union = []
            q = deque()
            q.append((i, j))
            union.append((i, j))
            temp_graph[i][j] = color
            while q:

                x, y = q.popleft()
                dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for d in dir:
                    nx = x + d[0]
                    ny = y + d[1]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or temp_graph[nx][ny] > 0:
                        continue
                    if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                        # print(f"{x}, {y} | {nx}, {ny}")
                        # print(f"abs = {abs(graph[x][y] - graph[nx][ny])}")

                        q.append((nx, ny))
                        union.append((x, y))
                        temp_graph[nx][ny] = color

            if len(union) == 1:
                count_noU += 1
                continue
            else:
                count += 1
                sum_union = 0

                set_union = set(union)
                union = list(set_union)
                print(sorted(union))
                for u in union:
                    sum_union += graph[u[0]][u[1]]

                print(sum_union, len(union))
                new_population = sum_union // len(union)

                for u in union:
                    graph[u[0]][u[1]] = new_population
                print(new_population)
                display(graph)
    # for un in union_list:
    #     for u in un:
    #         sum_union += graph[u[0]][u[1]]
    #
    #     print(sum_union, len(un))
    #     new_population = sum_union // len(un)
    #
    #     for u in un:
    #         graph[u[0]][u[1]] = new_population
    #     print(new_population)
    #     print(graph)

print(count)
