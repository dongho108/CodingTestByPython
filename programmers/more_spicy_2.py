import heapq


def solution(scoville, K):
    answer = 0

    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    flag = False
    # print(heap)
    while heap:
        a = heapq.heappop(heap)

        if a >= K:
            flag = True
            break

        if len(heap) == 0:
            flag = False
            break

        b = heapq.heappop(heap)
        # print(a, b, a+b*2)
        heapq.heappush(heap, a + b * 2)
        answer += 1
        # print(heap)

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