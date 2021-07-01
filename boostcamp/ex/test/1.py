def solution(v):
    answer = []

    x_dict = dict()
    y_dict = dict()

    for i in range(len(v)):
        x, y = v[i]

        if x_dict.get(x) is None:
            x_dict[x] = 1
        else:
            x_dict[x] = 2

        if y_dict.get(y) is None:
            y_dict[y] = 1
        else:
            y_dict[y] = 2

    for i in x_dict.keys():
        if x_dict[i] == 1:
            answer.append(i)
            break

    for i in y_dict.keys():
        if y_dict[i] == 1:
            answer.append(i)
            break

    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))