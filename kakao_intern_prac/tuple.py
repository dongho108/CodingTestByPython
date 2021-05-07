def solution(s):
    answer = []

    s = list(s)

    stack = []
    stack.append(s[0])

    i = 1
    data_list = []
    while True:
        if s[i] == '}':
            # 끝내기
            if stack == ['{']:
                stack.pop()
                break

            # 들어있던 숫자들 빼기
            data = []
            number = []
            j = len(stack)-1
            while stack[j] != '{':
                # print(stack)
                # print(f"j = {j}, stack[j] = {stack[j]}")

                if stack[j] == ',':
                    data.append(int(''.join(reversed(number))))
                    # print(f"data = {data}")
                    # print(f"=={stack}")
                    stack.pop()
                    # print(f"=={stack}")
                    number = []
                else:
                    number.append(stack.pop())
                    # print(f"number = {number}")
                j -= 1
            # print(f"$$stack = {stack}")
            data.append(int(''.join(reversed(number))))
            # print(f"data = {data}")
            stack.pop()
            if stack[-1] == ',':
                stack.pop()

            data_list.append(data)
            # print(data_list)
        else:
            stack.append(s[i])

        i += 1

    # print(data_list)

    data_list.sort(key=lambda x:len(x))

    for i in range(len(data_list)):

        for j in range(len(answer)):
            data_list[i].remove(answer[j])

        answer.append(data_list[i][0])

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution())