def solution(N, stages):
    answer = []
    length = len(stages)

    count = [0 for _ in range(N+1)]

    for s in stages:
        if len(count) <= s:
            continue
        count[s] += 1

    results = []
    for i in range(1, N+1):
        if length == 0:
            cal = 0
        else:
            cal = float(count[i] / length)
        length -= count[i]
        results.append((i, cal))

    print(results)
    results.sort(key=lambda x:x[1], reverse=True)

    # print(results)

    answer = [i[0] for i in results]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))