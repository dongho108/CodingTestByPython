from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)

for i in range(1, n+1):
    x_tuple = list(map(int, input().split()))
    time[i] = x_tuple[0]

    for j in x_tuple[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

print(indegree)


q = deque()
result = []

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for g in graph[now]:
        indegree[g] -= 1
        if indegree[g] == 0:
            q.append(g)

for r in result:
    print(r, end=' ')


'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''