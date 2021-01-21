from itertools import combinations

def dfs(graph, start):
    x = start[0]
    y = start[1]

    graph[x][y] = 2

    # 상 하 좌 우
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for d in dir:
        nowx = x+d[0]
        nowy = y+d[1]

        if nowx < 0 or nowx >= n or nowy < 0 or nowy >= m:
            continue

        if graph[nowx][nowy] == 0:
            dfs(graph, [nowx, nowy])


def initLab(sourceLab):
    reLab = [[0]*len(sourceLab[0]) for i in range(len(sourceLab))]
    for i in range(len(sourceLab)):
        for j in range(len(sourceLab[0])):
            reLab[i][j] = sourceLab[i][j]
    return reLab


n, m = map(int, input().split())

lab = []
zero = []
start = []
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(m):
        if lab[i][j] == 0:
            zero.append([i, j])
        if lab[i][j] == 2:
           start.append([i, j])

pickwall = list(combinations(zero, 3))

result = []
# 벽 세개 세우는 경우 다 해보기
for i in range(len(pickwall)):

    tempLab = initLab(lab)
    for p in pickwall[i]:
        x = p[0]
        y = p[1]

        tempLab[x][y] = 1

    # 모든 바이러스로부터 시작
    for st in start:
        dfs(tempLab, st)

    # 안전지대 개수 세기
    count = 0
    for j in range(n):
        for k in range(m):
            if tempLab[j][k] == 0:
                count += 1
    result.append(count)

print(max(result))



