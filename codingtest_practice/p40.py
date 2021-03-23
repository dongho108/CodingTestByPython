import heapq


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

INF = int(1e9)
distance = [INF] * (n+1)
q = []
q.append((0, 1))
distance[1] = 0

while q:
    dist, x = heapq.heappop(q)

    if distance[x] < dist:
        continue

    for g in graph[x]:
        cost = dist + g[0]
        if cost < distance[g[1]]:
            distance[g[1]] = cost
            heapq.heappush(q, (cost, g[1]))

result_number = 0
result_dist = 0
result_sameNum = 0

distance[0] = -1
max_value = max(distance)
for i in range(len(distance)-1, 0, -1):
    if distance[i] == max_value:
        result_number = i
        result_dist = distance[i]
        result_sameNum += 1

print(result_number, result_dist, result_sameNum)

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''