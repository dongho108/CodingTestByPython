def exit(ptr, progresses, exit_check):
    exit_check[ptr] = True
    count = 1
    new_ptr = ptr + 1
    first_check = False

    for i in range(ptr + 1, len(progresses)):
        if progresses[i] >= 100:
            if not first_check:
                new_ptr = i
                first_check = True
            exit_check[i] = True
            count += 1
        else:
            break

    # print(ptr, new_ptr, count, exit_check, progresses)

    return (new_ptr, count)


def solution(progresses, speeds):
    answer = []

    length = len(progresses)

    exit_check = [False for _ in range(length)]

    exit_count = 0
    ptr = 0

    while exit_count < length:
        for i in range(length):
            if progresses[i] < 100:
                progresses[i] += speeds[i]

        if progresses[ptr] >= 100:
            ptr, count = exit(ptr, progresses, exit_check)
            exit_count += count
            answer.append(count)

    return answer
