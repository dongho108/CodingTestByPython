def cal(pre, now, exp):
    print(f"{pre}, {now}, {exp}")
    if exp == '*':
        return pre * now
    elif exp == '+':
        return pre + now
    else:
        return pre - now


def solution(expression):
    answer = 0

    oper_list = [['*', '+', '-'],
                 ['*', '-', '+'],
                 ['+', '*', '-'],
                 ['+', '-', '*'],
                 ['-', '+', '*'],
                 ['-', '*', '+']]

    # 연산자 우선 순위 바꿔가며
    for oper in oper_list:
        expression_list = list(expression)

        # 우선순위 차례로 진행
        for op in oper:
            print(f"now op = {op}")
            number_list = []
            exp_list = []
            number = ""
            next = False
            pre = -1
            # expression 파싱
            for exp in expression_list:
                print(f"now : {exp}")
                # 연산자일때
                if exp in oper:
                    # 이 전 연산자가 우선순위였을때 계산
                    if next:
                        now = int(number)
                        number_list.pop()
                        cal_result = cal(pre, now, op)
                        if len(number_list) == 0:
                            number_list.append(str(cal_result))
                        else:
                            number_list.append(str(abs(cal_result)))
                        next = False
                    else:
                        number_list.append(number)

                    # 현재 우선순위 연산자일때
                    if exp == op:
                        pre = int(number)
                        next = True
                    else:
                        exp_list.append(exp)
                    number = ""
                else:  # 숫자일때
                    number += exp
            if next:
                now = int(number)
                number_list.pop()
                cal_result = cal(pre, now, op)
                if len(number_list) == 0:
                    number_list.append(str(cal_result))
                else:
                    number_list.append(str(abs(cal_result)))
            else:
                number_list.append(number)
            expression_list = number_list[0]
            print(number_list)
            print(exp_list)
            for i in range(len(exp_list)):
                expression_list += exp_list[i]
                expression_list += number_list[i+1]


    return answer

print(solution("100-200*300-500+20"))