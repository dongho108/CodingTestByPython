from collections import deque

def solution(n, passenger, train):
    answer = []

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    distance = [0] * (n+1)

    for i in range(len(train)):
        a, b = train[i]
        graph[a].append(b)

    path = [-1] * (n+1)

    q = deque()
    q.append((1, 1))

    while q:
        dist, now = q.popleft()
        visited[now] = True
        distance[now] = dist

        for i in graph[now]:
            if not visited[i]:
                q.append((dist+1, i))
                visited[i] = True
                path[i] = now

    max_value = 0
    max_index = -1
    for i in range(n, 0, -1):
        if max_value < distance[i]:
            max_value = distance[i]
            max_index = i

    answer.append(max_index)

    next = max_index
    result = 0
    while next != -1:
        result += passenger[next-1]
        next = path[next]

    answer.append(result)


    return answer

print(solution(6, [1,1,1,1,1,1], [[1,2],[1,3],[1,4],[3,5],[3,6]]))
print(solution(4, [2,1,2,2], [[1,2],[1,3],[2,4]]))
print(solution(5, [1,1,2,3,4], [[1,2],[1,3],[1,4],[1,5]]))