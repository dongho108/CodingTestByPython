def dfs(x, y):
    data[x][y] = '1'
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in dir:
        nx = x+d[0]
        ny = y+d[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if data[nx][ny] != '1':
            dfs(nx, ny)


n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(input()))

result = 0
print(data[13][3])
for i in range(n):
    for j in range(m):
        if data[i][j] == '0':
            dfs(i, j)
            result += 1

print(result)



'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''