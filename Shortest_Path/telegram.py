import sys
import heapq

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # i[0] : now와 연결된 노드 번호
            # i[1] : 까지 소요되는 비용
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count_city = 0
count_cost = 0
for i in range(1, n+1):
    if distance[i] != INF:
        count_city += 1
        if count_cost < distance[i]:
            count_cost = distance[i]

print(count_city-1, count_cost)
