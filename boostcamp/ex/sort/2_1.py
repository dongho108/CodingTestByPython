def solution(numbers):
    answer = ''

    numbers.sort(key=lambda x:str(x)*3, reverse=True)

    for number in numbers:
        answer += str(number)

    answer = str(int(answer))
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0]))