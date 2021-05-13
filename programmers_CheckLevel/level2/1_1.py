def solution(prices):
    answer = [0 for i in range(len(prices))]

    num = 1
    for i in range(len(prices)-2, -1, -1):
        if prices[i] == 1:
            answer[i] = num
            num += 1
            continue
        if prices[i] <= prices[i+1]:
            count = 1
            plag = True
            for j in range(i + 1, len(prices)):
                if prices[i] <= prices[j]:
                    count += 1
                else:
                    answer[i] = count
                    plag = False
                    break

            if plag:
                answer[i] = count-1
            else:
                answer[i] = count
        else:
            answer[i] = 1
        num += 1

    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([3, 1, 4, 3, 4, 2]))