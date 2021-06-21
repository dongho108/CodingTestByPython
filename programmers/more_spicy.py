import heapq


def solution(scoville, K):
    answer = 0

    flag = False
    scoville.sort()

    # print(scoville)
    while scoville:
        a = heapq.heappop(scoville)

        if a >= K:
            flag = True
            break

        if len(scoville) == 0:
            flag = False
            break

        b = heapq.heappop(scoville)
        # print(a, b, a+b*2)
        heapq.heappush(scoville, a+b*2)
        answer += 1
        # print(scoville)

    if flag:
        return answer
    else:
        return -1


# print(solution([1, 2, 3, 9, 10, 12], 7))
# print(solution([1, 2], 7))
# print(solution([10, 12], 7))
# print(solution([1, 1, 1, 1, 1, 1], 20))
# print(solution([3, 4, 8, 9, 10, 12], 7))
print(solution([1,1], 10))