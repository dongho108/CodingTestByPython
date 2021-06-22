def dfs(depth, dfs_sum, numbers, target, ans_array):
    # print(depth, dfs_sum)
    if depth == len(numbers):
        if dfs_sum == target:
            # print("check")
            ans_array[0] += 1
        return
    # print(depth, dfs_sum, numbers, target, ans_array)
    dfs(depth+1, dfs_sum + numbers[depth], numbers, target, ans_array)
    dfs(depth+1, dfs_sum - numbers[depth], numbers, target, ans_array)


def solution(numbers, target):
    answer = [0]
    dfs(0, 0, numbers, target, answer)

    return answer[0]


print(solution([1, 1, 1, 1, 1], 3))
# print(solution([1, 2, 3, 4, 5], 3))