def solution(gems):
    item_size = len(set(gems))

    l, r = 0, 0

    item_map = dict()
    item_map[gems[0]] = 1

    result = [0, len(gems)-1]

    while l < len(gems) and r < len(gems):
        if len(item_map) == item_size:
            if r - l < result[1] - result[0]:
                result[1] = r
                result[0] = l
            if item_map[gems[l]] == 1:
                del item_map[gems[l]]
            else:
                item_map[gems[l]] -= 1
            l += 1
        else:
            r += 1
            if r == len(gems):
                break
            if gems[r] in item_map.keys():
                item_map[gems[r]] += 1
            else:
                item_map[gems[r]] = 1
    return [result[0]+1, result[1]+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))