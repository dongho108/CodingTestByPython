def solution(n):
    answer = ''

    while n > 0:
        r = n % 3
        n = n // 3

        if r == 0:
            r = 4
            n -= 1

        answer = str(r) + answer

    return answer

print(solution(4))