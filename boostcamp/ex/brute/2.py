from itertools import permutations
import math


def check_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    numbers_list = list(numbers)
    number_set = set()

    for i in range(1, len(numbers_list)+1):
        numbers_perm = list(permutations(numbers_list, i))
        for j in range(len(numbers_perm)):
            number_set.add(int(''.join(numbers_perm[j])))

    # print(number_set)

    while number_set:
        if check_prime(number_set.pop()):
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))