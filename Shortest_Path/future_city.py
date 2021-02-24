n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())


for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end='\t')
    print()

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])


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