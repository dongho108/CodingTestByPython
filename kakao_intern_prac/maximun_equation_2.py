def cal(pre, now, exp):
    # print(f"{pre}, {now}, {exp}")
    if exp == '*':
        return pre * now
    elif exp == '+':
        return pre + now
    else:
        return pre - now


def solution(expression):
    answer = 0
    expression = list(expression)

    num_list = []
    exp_list = []

    number = ""

    exp = ['*', '-', '+']

    for i in expression:
        if i in exp:
            if number:
                num_list.append(int(number))
                number = ""
            exp_list.append(i)
        else:
            number += i
    if number:
        num_list.append(int(number))

    oper_list = [['*', '+', '-'],
                 ['*', '-', '+'],
                 ['+', '*', '-'],
                 ['+', '-', '*'],
                 ['-', '+', '*'],
                 ['-', '*', '+']]

    max_value = 0
    for oper in oper_list:
        t_num_list = []
        for i in range(len(num_list)):
            t_num_list.append(num_list[i])

        t_exp_list = []
        for i in range(len(exp_list)):
            t_exp_list.append(exp_list[i])

        for op in oper:
            i = 0
            while i < len(t_exp_list):
                if t_exp_list[i] == op:
                    result = cal(t_num_list.pop(i), t_num_list.pop(i), t_exp_list.pop(i))
                    t_num_list.insert(i, result)
                    i -= 1
                    # print(t_num_list, t_exp_list)
                i += 1

        if max_value < abs(t_num_list[0]):
            max_value = abs(t_num_list[0])
            # print(f"max_value = {max_value}")

    answer = max_value
    return answer

print(solution("100-200*300-500+20"))

# if len(t_num_list) > 1:
#     result = cal(t_num_list.pop(0), t_num_list.pop(0), op)
#     t_exp_list.pop(0)
#     t_num_list.insert(0, result)
#     print(t_num_list, t_exp_list)