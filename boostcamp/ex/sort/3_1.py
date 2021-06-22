def solution(citations):
    answer = 0

    if sum(citations) == 0:
        return answer

    now_count = 0
    now_num = -1

    citations.sort(reverse=True)
    for i in range(len(citations)):
        now_count += 1
        now_num = citations[i]

        # print(now_count, now_num)
        if now_count > now_num:
            answer = now_count-1
            break

    if answer == 0:
        answer = len(citations)

    return answer

# print(solution([3, 0, 6, 1, 5]))
# print(solution([5, 5, 5, 5, 5, 3, 2, 1]))
# print(solution([6, 5, 5, 5, 4, 3, 2, 1]))
print(solution([20, 19, 18, 5, 5, 5, 4, 1]))
print(solution([20,19,18,1]))
print(solution([20,19,18,3]))
print(solution([20,19,18,17]))
print(solution([0,0,0,0]))