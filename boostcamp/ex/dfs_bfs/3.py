def dfs(start, graph, visited, answer):
    visited[start] = True
    print(start)
    check = 0
    for g in graph[start]:
        if not visited[g]:
            dfs(visited[g], graph, visited, answer)
        else:
            check += 1

    if check == len(graph[start]):
        answer[0] += 1


def solution(n, computers):
    answer = [0]

    graph = [[] for i in range(len(computers))]

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)

    visited = [False for _ in range(len(computers))]

    for i in range(len(computers)):
        if not visited[i]:
            dfs(i, graph, visited, answer)

    return answer[0]


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))