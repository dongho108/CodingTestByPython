n, m = map(int, input().split())
x, y, d = map(int, input().split())

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

visit = [[0] * m for _ in range(n)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
turn_count = 0
count = 1

visit[x][y] = 1
while True:
    d = (d+3) % 4
    turn_count += 1
    next_x = x + dir[d][0]
    next_y = y + dir[d][1]

    if game_map[next_x][next_y] != 1 and 0 <= next_x < n and 0 <= next_y < m and visit[next_x][next_y] != 1:
        x = next_x
        y = next_y
        visit[x][y] = 1
        turn_count = 0
        count += 1
    else:
        if turn_count == 4:
            temp_d = (d+2) % 4
            temp_x = x + dir[temp_d][0]
            temp_y = y + dir[temp_d][1]
            
            if game_map[temp_x][temp_y] != 1 and 0 <= temp_x < n and 0 <= temp_y < m:
                x = temp_x
                y = temp_y
                turn_count = 0
            else:
                break
        else:
            continue

print(count)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''