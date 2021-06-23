n = int(input())
target = int(input())

data = [[0] * n for _ in range(n)]

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

x, y = 0, 0
value = n*n

now_num = 0
now_dir = 0

target_x = -1
target_y = -1
while now_num < 4:
    data[x][y] = value
    if value == target:
        target_x = x+1
        target_y = y+1

    nx = x + dir[now_dir%4][0]
    ny = y + dir[now_dir%4][1]

    if nx < 0 or ny < 0 or n <= nx or n <= ny or data[nx][ny] != 0: # 벽
        now_num += 1
        now_dir += 1
    else:
        now_num = 0
        x = nx
        y = ny
        value -= 1

for i in range(n):
    for j in range(n):
        print(data[i][j], end=' ')
    print()
print(target_x, target_y)