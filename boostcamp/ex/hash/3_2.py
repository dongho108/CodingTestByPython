def solution(clothes):
    count = 1

    cloth_dict = dict()

    for name, group in clothes:
        if cloth_dict.get(group) is None:
            cloth_dict[group] = list()
        cloth_dict[group].append(name)

    for group in cloth_dict:
        count *= (len(cloth_dict[group])+1)

    return count-1


print(solution([["yellowhat", "headgear"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["a", "up"], ["c", "down"], ["d", "down"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["c", "down"], ["d", "down"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))