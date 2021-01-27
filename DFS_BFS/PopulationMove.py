from collections import deque

def display(tl):
    for i in range(n):
        for j in range(n):
            print(tl[i][j], end=' ')
        print()


n, l, r = map(int, input().split())
world = []
for i in range(n):
    world.append(list(map(int, input().split())))

check = True
result = 0
while check:
# for __ in range(3):
#     print("--world")
    # display(world)
    result += 1
    # print(f"result = {result}")

    queue = deque()
    tempWorld = [[0]*n for _ in range(n)]

    # 상 하 좌 우
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # sameContries = []
    color = 0
    checkCount = 0

    for i in range(n):
        for j in range(n):

            if tempWorld[i][j] == 0:
                sameContries = []
                color += 1
                queue.append([i, j])
                total = world[i][j]
                # print(f"total = {total}")
                while queue:
                    # print(queue)
                    # print("--temworld")
                    # display(tempWorld)
                    pre = queue.popleft()
                    # print(f"pre = {pre}")
                    sameContries.append(pre)
                    tempWorld[pre[0]][pre[1]] = color

                    for d in dir:
                        nowX = pre[0]+d[0]
                        nowY = pre[1]+d[1]
                        if nowX < 0 or nowY < 0 or nowX >= n or nowY >= n or tempWorld[nowX][nowY] != 0:
                            continue
                        diff = abs(world[pre[0]][pre[1]] - world[nowX][nowY])
                        # print(f"{world[pre[0]][pre[1]]} - {world[nowX][nowY]} diff = {diff}")
                        if l <= diff <= r:
                            queue.append([nowX, nowY])
                            tempWorld[nowX][nowY] = color

                            total += world[nowX][nowY]
                            # print(f"total = {total}")
                            checkCount += 1
                # sameContries.append(sameContry)

                for a, b in sameContries:
                    # print(f"{total} / {len(sameContries)}")
                    world[a][b] = total // len(sameContries)

    if checkCount == 0:
        check = False

print(result-1)
