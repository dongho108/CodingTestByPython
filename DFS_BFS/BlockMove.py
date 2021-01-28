from collections import deque

def display(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()


def get_next(st, n_b):

    get = []
    dir = [[0, -1], [0, 1], [1, 0], [-1, 0]]

    st = list(st)
    now_x1, now_y1, now_x2, now_y2 = st[0][0], st[0][1], st[1][0], st[1][1]

    for d in dir:
        next_x1 = now_x1+d[0]
        next_y1 = now_y1+d[1]
        next_x2 = now_x2+d[0]
        next_y2 = now_y2+d[1]

        if n_b[next_x1][next_y1] == 0 and n_b[next_x2][next_y2] == 0:
            get.append({(next_x1, next_y1), (next_x2, next_y2)})

    # 막대가 가로
    if now_x1 == now_x2:
        # 위, 아래
        for i in [-1, 1]:
            if n_b[now_x1 + i][now_y1] == 0 and n_b[now_x2 + i][now_y2] == 0:
                get.append({(now_x1, now_y1), (now_x1+i, now_y1)})
                get.append({(now_x2, now_y2), (now_x2+i, now_y2)})
    elif now_y1 == now_y2:
        # 오른쪽, 왼쪽
        for i in [-1, 1]:
            if n_b[now_x1][now_y1+i] == 0 and n_b[now_x2][now_y2+i] == 0:
                get.append({(now_x2, now_y2), (now_x2, now_y2+i)})
                get.append({(now_x1, now_y1), (now_x1, now_y1+i)})
    return get





def solution(board):
    n = len(board)

    new_board = [[0] * (n+2) for _ in range(n+2)]

    for i in range(n+2):
        for j in range(n+2):
            if i == 0 or i == n+1 or j == 0 or j == n+1:
                new_board[i][j] = 1
            else:
                new_board[i][j] = board[i-1][j-1]

    # display(board)
    # display(new_board)

    start = {(1, 1), (1, 2)}
    visited = []

    queue = deque()
    queue.append((start, 0))
    visited.append(start)

    while queue:
        start, count = queue.popleft()
        # print(f"start = {start}, count = {count}")
        if (n, n) in start:
            return count

        for next in get_next(start, new_board):
            # print(f"next = {next}")
            if next not in visited:
                queue.append((next, count+1))
                visited.append(next)


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))