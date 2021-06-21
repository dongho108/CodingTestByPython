def first_num(x):
    if x < 10:
        return x
    elif 10 <= x < 100:
        return x // 10
    elif 100 <= x < 1000:
        return x // 100
    else:
        return x // 1000


def solution(numbers):
    answer = ''
    semi_answer = ''

    numbers.sort(key=lambda x:(first_num(x), ), reverse=True)

    for i in range(len(numbers)):
        answer += str(numbers[i])

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))