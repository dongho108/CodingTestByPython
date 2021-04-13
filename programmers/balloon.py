import heapq


def solution(a):
    answer = 0

    for i in range(len(a)):
        if i == 0 or i == len(a)-1:
            answer += 1
            continue
        left = a[:i]
        right = a[i+1:]
        heapq.heapify(left)
        heapq.heapify(right)
        left_min = heapq.heappop(left)
        right_min = heapq.heappop(right)
        temp = [left_min, right_min, a[i]]
        if max(temp) != a[i]:
            answer += 1

    return answer


print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
