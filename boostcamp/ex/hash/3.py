from itertools import combinations


def solution(clothes):
    count = 0

    cloth_dict = dict()

    for name, group in clothes:
        if group not in cloth_dict.keys():
            cloth_dict[group] = list()
        cloth_dict[group].append(name)
        count += 1

    for i in range(2, len(cloth_dict.keys())+1):
        keys_list = list(combinations(list(cloth_dict.keys()), i))

        for cloth_tuple in keys_list:
            print(cloth_tuple)
            mul = 1
            for j in range(i):
                # print(cloth_dict[cloth_tuple[j]])
                mul *= len(cloth_dict[cloth_tuple[j]])
            print(mul)
            count = count + mul
            # print(count)

    return count


# print(solution([["yellowhat", "headgear"]]))
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["a", "up"], ["c", "down"], ["d", "down"]]))
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["c", "down"], ["d", "down"]]))
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))