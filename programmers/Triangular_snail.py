def solution(n):
    answer = []

    graph = [[0]*n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    dir = [[-1, -1], [1, 0], [0, 1]]
    dir_count = 0

    br = 0
    x, y = 0, 0
    data = 1
    while True:
        graph[x][y] = data
        visited[x][y] = True

        nx = x + dir[dir_count][0]
        ny = y + dir[dir_count][1]
        # print(graph)
        while nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == True:
            if br == 2:
                break
            # print(br)
            dir_count = (dir_count + 1) % 3
            br += 1
            nx = x + dir[dir_count][0]
            ny = y + dir[dir_count][1]
            # print(nx, ny)

        if br == 2:
            break

        br = 0
        x = nx
        y = ny
        data += 1

    # print(graph)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                break
            answer.append(graph[i][j])

    return answer

print(solution(1))
print(solution(2))

print(solution(3))

print(solution(4))
print(solution(5))
print(solution(6))