def dfs(start, n, computers, visited):
    visited[start] = True

    for i in range(n):
        if computers[start][i] == 1 and visited[i] == False:
            dfs(i, n, computers, visited)




def solution(n, computers):
    answer = 0

    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            dfs(i, n, computers, visited)
            answer += 1



    return answer