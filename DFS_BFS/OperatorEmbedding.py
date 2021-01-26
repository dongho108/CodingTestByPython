from itertools import permutations



def calculator(numbers, ops):
    pre = numbers[0]
    for i in range(1, len(numbers)):
        j = i-1

        if ops[j] == "+":
            pre = pre + numbers[i]
        elif ops[j] == "-":
            pre = pre - numbers[i]
        elif ops[j] == "*":
            pre = pre * numbers[i]
        elif ops[j] == "/":
            # if pre < 0:
            #     print(numbers[j], numbers[i])
            if pre < 0 and numbers[i] > 0:
                pre = abs(pre)
                pre = -(pre // numbers[i])
            else:
                pre = pre // numbers[i]
    # print(numbers, ops)
    # print(pre)
    # print("----")
    return pre

n = int(input())
nums = list(map(int, input().split()))
numOperator = list(map(int, input().split()))



operators = []
for i in range(len(numOperator)):
    for j in range(numOperator[i]):
        if i == 0:
            operators.append("+")
        elif i == 1:
            operators.append("-")
        elif i == 2:
            operators.append("*")
        elif i == 3:
            operators.append("/")

pickop = list(permutations(operators, n-1))

results = []
for op in pickop:
    results.append(calculator(nums, op))

print(max(results))
print(min(results))
