import heapq


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return distance[end]


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())

distance = [INF] * (n+1)
a = dijkstra(1, k)
distance = [INF] * (n+1)
b = dijkstra(k, x)

print(a, b)
print(a+b)


'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''