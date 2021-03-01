

def dfs(graph, start, visited, st):
    visited[start] = True
    st += skill[start]+" "

    if len(graph[start]) == 0:
        print(st)

    for i in graph[start]:
        if not visited[skill.index(i)]:
            dfs(graph, skill.index(i), visited, st)


skill = list(input().split())
n = int(input())
graph = [[] for _ in range(len(skill))]


for i in range(n):
    a, b = input().split()
    graph[skill.index(a)].append(b)

visited = [False] * len(skill)

st = ""
dfs(graph, 0, visited, st)

