def rate_check(x):
    if x == 6:
        return 1
    elif x == 5:
        return 2
    elif x == 4:
        return 3
    elif x == 3:
        return 4
    elif x == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []

    lottos.sort()
    win_nums.sort()

    zero_count = 0
    same_count = 0

    while lottos[0] == 0:
        zero_count += 1
        lottos.pop(0)

    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if win_nums[j] == lottos[i]:
                same_count += 1
                break

    maximun_rate = zero_count + same_count
    minimun_rate = same_count

    answer.append(rate_check(maximun_rate))
    answer.append(rate_check(minimun_rate))

    return answer

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))