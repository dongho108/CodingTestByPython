def solution(a):
    answer = 0

    min_list = [[] for _ in range(len(a))]
    min_value = int(1e9)

    for i in range(len(a)):
        if a[i] < min_value:
            min_list[i].append(a[i])
            min_value = a[i]
        else:
            min_list[i].append(min_value)

    min_value = int(1e9)
    for i in range(len(a)-1, -1, -1):
        if a[i] < min_value:
            min_list[i].append(a[i])
            min_value = a[i]
        else:
            min_list[i].append(min_value)

    for i in range(len(a)):
        if a[i] <= min_list[i][0] or a[i] <= min_list[i][1]:
            answer += 1

    return answer


print(solution([3, 1, -5]))
print(solution([9, -1, 1, 5]))

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
