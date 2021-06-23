n, m = map(int, input().split())
answer = ""

data = []
for i in range(n):
    data.append(list(input()))

up_count = 0
down_count = 0
left_point = -1
right_point = -1
left_right_mode = False
up_search = True

for i in range(n):
    sharp_count = 0
    # print(left_point, right_point)

    if not left_right_mode:
        first_search = True # True이면 왼쪽포인트, False 이면 오른쪽 포인
        for j in range(m):
            if data[i][j] == '#':
                if first_search:
                    left_point = j
                    first_search = False
                sharp_count += 1
            else:
                if left_point != -1:
                    right_point = j - 1

        if sharp_count >= 3:
            if up_search:
                up_count = sharp_count
                left_right_mode = True
                up_search = False
    else:
        save_point = []
        for j in range(m):
            if data[i][j] == '#':
                save_point.append(j)
                sharp_count += 1
        if sharp_count == 1:
            if save_point[0] == left_point:
                answer = "RIGHT"
            else:
                answer = "LEFT"
            break
        if sharp_count >= 3:
            down_count = sharp_count
            if up_count < down_count:
                answer = "UP"
            else:
                answer = "DOWN"
            break

print(answer)
