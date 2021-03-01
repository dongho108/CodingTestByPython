a, b = map(int, input().split())

count = 0

while a != b:
    check = b - a
    if check == 0:
        break
    elif check > 0: # 온도 올리기
        if 1 <= check <= 2:
            a += 1
        elif 3 <= check <= 7:
            a += 5
        else:
            a += 10
        count += 1
    else: # 온도 내리기
        if -2 <= check <= -1:
            a -= 1
        elif -7 <= check <= -3:
            a -= 5
        else:
            a -= 10
        count += 1

print(count)