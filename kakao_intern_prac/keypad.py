def dist(now_dir, n):
    return abs(now_dir[0]-n[0]) + abs(now_dir[1]-n[1])


def solution(numbers, hand):
    answer = ''
    pad = [[0] * 3 for _ in range(4)]
    reverse_pad = [0] * 13
    count = 1

    for i in range(4):
        for j in range(3):
            pad[i][j] = count
            reverse_pad[count] = (i, j)
            count += 1
    reverse_pad[0] = (3, 1)
    # print(reverse_pad)

    left_hand = [1, 4, 7]
    right_hand = [3, 6, 9]

    now_left = [3, 0]
    now_right = [3, 2]

    for number in numbers:
        print(f"number : {number}")
        print(f"now dir = {now_left}, {now_right}")
        if number in left_hand:
            answer += 'L'
            now_left = reverse_pad[number]
        elif number in right_hand:
            answer += 'R'
            now_right = reverse_pad[number]
        else:
            if dist(now_left, reverse_pad[number]) < dist(now_right, reverse_pad[number]):
                answer += 'L'
                now_left = reverse_pad[number]
            elif dist(now_left, reverse_pad[number]) > dist(now_right, reverse_pad[number]):
                answer += 'R'
                now_right = reverse_pad[number]
            else:
                if hand == "left":
                    answer += 'L'
                    now_left = reverse_pad[number]
                else:
                    answer += 'R'
                    now_right = reverse_pad[number]

    return answer


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
