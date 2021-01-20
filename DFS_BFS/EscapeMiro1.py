from collections import deque


def bfs(miro, x, y):
    queue = deque()
    queue.append([x, y])

    # 상 하 좌 우
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while queue:
        now = queue.popleft()

        for d in dir:
            nx = now[0] + d[0]
            ny = now[1] + d[1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if miro[nx][ny] == 1:
                queue.append([nx, ny])
                miro[nx][ny] = miro[now[0]][now[1]] + 1



n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

bfs(miro, 0, 0)
print(miro[n-1][m-1])



"""
5 6
101010
111111
000001
111111
111111
"""