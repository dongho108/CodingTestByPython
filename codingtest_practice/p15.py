from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

data = [0] * (n+1)
visited = [False] * (n+1)
q = deque()

q.append(x)
visited[x] = True


while q:

    now = q.popleft()
    visited[now] = True

    if not graph[now]:
        continue
    for g in graph[now]:
        if visited[g] == True:
            continue
        q.append(g)
        visited[g] = True
        data[g] = data[now] + 1

count = 0

for i in range(1, n+1):
    if data[i] == k:
        print(i)
    else:
        count += 1

if count == n:
    print(-1)
