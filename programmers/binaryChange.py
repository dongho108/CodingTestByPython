count = 0
delete_zero = 0


def binary_change(x):
    global count
    global delete_zero

    if len(x) == 1:
        return
    count += 1
    x.sort()
    i = 0
    while x[i] == '0':
        x.pop(0)
        delete_zero += 1
    length = len(x)

    b = str(format(length, 'b'))
    binary_change(list(b))


def solution(s):
    answer = []

    binary_change(list(s))
    answer.append(count)
    answer.append(delete_zero)
    return answer

# print(solution("110010101001"))
# print(solution("01110"))
print(solution("1111111"))