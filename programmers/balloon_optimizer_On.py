def solution(a):
    answer = 2

    left_min = a[0]
    right_min = a[-1]
    length = len(a)

    if length == 1:
        answer = 1
        return answer

    i = 1
    j = length-2

    while i <= j:

        if a[i] < max(left_min, right_min):
            answer += 1
            if a[i] < left_min:
                left_min = a[i]
        i += 1

        if a[j] < max(left_min, right_min):
            answer += 1
            if a[j] < right_min:
                right_min = a[j]
        j -= 1

    return answer

print(solution([3, 1, -5]))
print(solution([9, -1, 1, 5]))

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
