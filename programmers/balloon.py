def solution(a):
    answer = 0

    for i in range(len(a)):
        if i == 0 or i == len(a)-1:
            answer += 1
            continue
        left_min = min(a[:i])
        right_min = min(a[i+1:])
        temp = [left_min, right_min, a[i]]
        if max(temp) != a[i]:
            answer += 1

    return answer


print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
