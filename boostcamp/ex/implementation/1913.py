n = int(input())
target = int(input())

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

data = [[0] * n for _ in range(n)]

value = 1
once = True

dir_count = 0
now_dir = 0

i, j = n // 2, n // 2
x, y = dir[now_dir]

test = 0

while [i, j] != [0, 0] and test < 30:
    test += 1
    data[i][j] = value
    # print(i, j)
    # print(data)
    value += 1

    if once:
        once = False
    else:
        once = True
        dir_count += 1

    x = dir[(now_dir + dir_count) % 4][0]
    y = dir[(now_dir + dir_count) % 4][1]
    print(x, y)
    i = i + x
    j = j + y

print(data)