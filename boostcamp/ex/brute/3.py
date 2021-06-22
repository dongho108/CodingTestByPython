def solution(brown, yellow):
    answer = []

    if yellow == 1:
        return [3, 3]

    for i in range(1, yellow):
        if yellow % i == 0:
            horiz = yellow // i
            vert = i
            cal_brown = (horiz+2)*2 + vert*2
            if brown == cal_brown:
                answer = [horiz+2, vert+2]
                break

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))