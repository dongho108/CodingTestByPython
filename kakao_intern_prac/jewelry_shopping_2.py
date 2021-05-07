def solution(gems):
    answer = []
    item_size = len(set(gems))

    item_map = dict()
    answer = [1, len(gems)]

    for i in range(len(gems)):
        item_map[gems[i]] = i+1
        if len(item_map) == item_size:
            # print(f"i = {i}")
            # print(item_map)
            min_value = min(item_map.values())
            max_value = max(item_map.values())
            # print(min_value, max_value, answer)
            if max_value - min_value < answer[1] - answer[0]:
                answer[0] = min_value
                answer[1] = max_value

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))