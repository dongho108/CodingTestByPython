from itertools import combinations
import heapq


def display(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            print(arr[i][j], end=' ')
        print()
    print("=====")


n, m, k = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]
road = []

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    road.append((a, b))


for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

pavement = list(combinations(road, k))


min_value = int(1e9)
for pave in pavement:
    temp_cost = []
    for dx, dy in pave:
        temp_cost.append((dx, dy, graph[dx][dy]))
        graph[dx][dy] = 0
        graph[dy][dx] = 0
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0


    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in range(1, n+1):
            if graph[now][i] != INF:
                cost = dist + graph[now][i]
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

    if min_value > distance[n]:
        min_value = distance[n]
    for dx, dy, dc, in temp_cost:
        graph[dx][dy] = dc
        graph[dy][dx] = dc


print(min_value)

