from itertools import combinations
from itertools import permutations
import math


def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    numbers_list = list(numbers)

    data = set()
    for i in range(1, len(numbers_list)+1):
        com_list = list(permutations(list(numbers), i))
        for j in range(len(com_list)):
            # data.add(int("".join(com_list[j])))
            number = "".join(com_list[j])
            if number != "":
                data.add(int("".join(com_list[j])))
            # print(number)

    data = list(data)

    for i in data:
        if is_prime_number(i):
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))