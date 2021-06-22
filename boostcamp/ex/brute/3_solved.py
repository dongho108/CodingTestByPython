def solution(brown, yellow):
    answer = []

    for i in range(1, yellow+1):
        if yellow % i == 0:
            x = i
            y = yellow // i

            tbrown = (x+2)*(y+2) - yellow
            if tbrown == brown:
                answer.append(y+2)
                answer.append(x+2)
                break

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))