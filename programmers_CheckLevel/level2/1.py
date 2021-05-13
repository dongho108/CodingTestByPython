def solution(prices):
    data = [[-1, True] for i in range(len(prices))]

    for i in range(len(prices)):
        data[i][0] += 1

        for j in range(0, i):
            if data[j][1] == True:
                if prices[i] < prices[j]:
                    data[j][0] += 1
                    data[j][1] = False
                else:
                    data[j][0] += 1
    answer = []
    for i in range(len(prices)):
        answer.append(data[i][0])

    return answer

print(solution([1, 2, 3, 2, 3]))