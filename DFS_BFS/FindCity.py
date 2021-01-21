from collections import deque

def bfs(x, graph, visited, dist):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        now = queue.popleft()
        if not graph[now]:
            continue
        for i in graph[now]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[now] + 1


n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    s, f = map(int, input().split())
    graph[s].append(f)

visited = [False]*(n+1)
dist = [0]*(n+1)
bfs(x, graph, visited, dist)
# print(visited)
# print(dist)
result = 0
for i in range(len(dist)):
    if dist[i] == k:
        result += 1
        print(i)
if result == 0:
    print(-1)

