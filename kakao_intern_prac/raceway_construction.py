import heapq


def solution(board):
    answer = 0

    num_st = 0
    num_cur = 0

    distance = [[int(1e9)]*len(board) for i in range(len(board))]

    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    q = []
    heapq.heappush(q, (0, (0, 0, -1)))
    distance[0][0] = 0

    while q:
        dist, (x, y, z) = heapq.heappop(q)
        # print(x, y, z)

        if distance[x][y] < dist:
            continue
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
                continue

            if board[nx][ny] == 1:
                continue

            cost = dist + 100

            num_st += 1
            # cost
            if z != -1:
                # 가로 -> x +- 1 일때 500원 추가
                if z == 0:
                    if d == (-1, 0) or d == (1, 0):
                        cost += 500
                else: # 세로 -> y +- 1 일때 500원 추가
                    if d == (0, -1) or d == (0, 1):
                        cost += 500
                num_cur += 1
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost

                # 아래 리스트들이 범위 벗어나는 경우 제외해야함
                if d[0] == 0 and (distance[x-d[0]][y-d[1]] == distance[x-1][y] or distance[x-d[0]][y-d[1]] == distance[x+1][y]):
                    nd = 0
                elif d[0] == 1 and (distance[x-d[0]][y-d[1]] == distance[x][y-1] or distance[x-d[0]][y-d[1]] == distance[x][y+1]):
                    nd = 1
                else:
                    if d[0] == 0:
                        nd = 0
                    else:
                        nd = 1

                print(nx, ny, nd)
                heapq.heappush(q, (cost, (nx, ny, nd)))


    print(distance)
    answer = distance[len(board)-1][len(board)-1]

    return answer

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))