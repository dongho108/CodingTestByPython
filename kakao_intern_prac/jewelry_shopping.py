def solution(gems):
    answer = []

    items = []
    for g in gems:
        if g not in items:
            items.append(g)

    start = 1
    end = len(gems)
    answer.append(start)
    answer.append(end)

    for i in range(len(gems)):
        if gems[i] in items:
            items.remove(gems[i])
            end = i+1
        else:
            if not items:
                answer[0] = start
                answer[1] = end

                break
            else:
                if gems[start-1] == gems[i]:
                    start += 1
                temp = gems[start-1]
                add_start = 0
                for j in range(start, end):
                    if temp == gems[j]:
                        add_start += 1
                    else:
                        break
                start += add_start
                end += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))