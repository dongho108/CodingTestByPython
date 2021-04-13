count_zero = 0
count_one = 0


def slice(arr, n):
    l = len(arr)
    temp = [[0] * (l // 2) for _ in range(l // 2)]

    if n == 0:
        for i in range(l // 2):
            for j in range(l // 2):
                temp[i][j] = arr[i][j]
    elif n == 1:
        for i in range(l // 2):
            for j in range((l // 2), l):
                temp[i][j - (l // 2)] = arr[i][j]
    elif n == 2:
        for i in range((l // 2), l):
            for j in range(l // 2):
                temp[i - (l // 2)][j] = arr[i][j]
    else:
        for i in range((l // 2), l):
            for j in range((l // 2), l):
                temp[i - (l // 2)][j - (l // 2)] = arr[i][j]
    return temp

def quad(arr):
    global count_zero
    global count_one

    l = len(arr)
    now = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != now:
                quad(slice(arr, 0))
                quad(slice(arr, 1))
                quad(slice(arr, 2))
                quad(slice(arr, 3))
                return

    # print(arr)
    if now == 0:
        count_zero += 1
    else:
        count_one += 1
    return



def solution(arr):
    answer = []
    quad(arr)
    answer.append(count_zero)
    answer.append(count_one)

    return answer


# print(solution([[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]))
# print(solution([[1,1,1,1], [1,1,1,1]]))
# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))