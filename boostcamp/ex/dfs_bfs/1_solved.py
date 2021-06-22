answer = 0

def dfs(n, sum, numbers, target):
    global answer
    if n == len(numbers):
        if sum == target:
            answer += 1
        return

    dfs(n+1, sum+numbers[n], numbers, target)
    dfs(n+1, sum-numbers[n], numbers, target)


def solution(numbers, target):
    global answer

    dfs(1, numbers[0], numbers, target)
    dfs(1, -numbers[0], numbers, target)

    return answer