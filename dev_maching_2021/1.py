def solution(lottos, win_nums):
    answer = []

    right = 0
    zero = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
            continue
        if lotto in win_nums:
            right += 1

    check = [6, 6, 5, 4, 3, 2, 1]


    answer.append(check[right+zero])
    answer.append(check[right])

    return answer
