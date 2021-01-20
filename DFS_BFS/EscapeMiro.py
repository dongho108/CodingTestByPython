result = 0

def dfs(miro, x, y):
    global result
    result += 1
    print(f"x, y = {x}, {y}")

    if x == n and y == m:
        return 1

    # 남 동 서 북
    dirx = [1, 0, 0, -1]
    diry = [0, 1, -1, 0]


    miro[x][y] = 0

    for i in range(len(dirx)):
        nowX = x+dirx[i]
        nowY = y+diry[i]

        if nowX < 1 or nowX > n or nowY < 1 or nowY > m:
            continue
        if miro[nowX][nowY] == 1:
            if dfs(miro, nowX, nowY) == 1:
                return 1
            else:
                return 0




n, m = map(int, input().split())

miro = []
miro.append([0]*m)
for i in range(1, n+1):
    miro.append(list(map(int, input())))
    miro[i].insert(0, 0)


dfs(miro, 1, 1)
print(result)
"""
5 6
101010
111111
000001
111111
111111
"""