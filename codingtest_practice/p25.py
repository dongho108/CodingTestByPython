def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count_i = stages.count(i)

        if length == 0:
            failure = 0
        else:
            failure = count_i / length

        length -= count_i
        answer.append((i, failure))

    answer.sort(key=lambda x:x[1], reverse=True)


    result = []
    for i in range(N):
        result.append(answer[i][0])

    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4, 4]))