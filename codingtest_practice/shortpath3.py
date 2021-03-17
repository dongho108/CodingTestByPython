import heapq

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []
q.append((0, c))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for g in graph[now]:
        cost = dist + g[1]
        if cost < distance[g[0]]:
            distance[g[0]] = cost
            heapq.heappush(q, (cost, g[0]))

city_count = 0
result = 0
for d in distance:
    if d != INF:
        city_count += 1
        if result < d:
            result = d

print(city_count, result)


'''
3 2 1
1 2 4
1 3 2
'''