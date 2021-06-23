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

    if left_right_mode:  # 왼, 오른쪽 변만 체크
        save_point = []
        for j in range(m):
            if data[i][j] == '#':
                save_point.append(j)
                sharp_count += 1
        if sharp_count >= 3:
            left_right_mode = False
            continue
        if len(save_point) == 1:
            print(save_point[0], left_point, right_point)
            if save_point[0] == left_point:
                answer = "RIGHT"
            else:
                answer = "LEFT"
            break

    else:
        first_search = True

        for j in range(m):
            # print(i, j)
            if data[i][j] == '#':
                if first_search:
                    left_point = j
                    print("left : ", left_point)
                    first_search = False
                    sharp_count += 1
            else:
                if left_point != -1:
                    right_point = j-1
                    print("right : ", right_point)

        if sharp_count >= 3:
            if up_search:
                up_count = sharp_count
                left_right_mode = True
                up_search = False
            else:
                down_count = sharp_count
                if up_count < down_count:
                    answer = "UP"
                else:
                    answer = "DOWN"
                break


print(answer)
