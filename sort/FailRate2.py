def solution(N, stages):
    answer = []
    length = len(stages)

    count = [0 for _ in range(N+1)]

    for s in stages:
        if len(count) <= s:
            continue
        count[s] += 1

    results = [(0, 0)]
    reachUser = 0
    for i in range(1, N+1):
        cal = float(count[i] / (length - reachUser))
        reachUser += count[i]
        results.append((i, cal))

    # print(results)
    results.sort(key=lambda x:x[1], reverse=True)

    # print(results)

    for r in results:
        if r[0] == 0:
            continue
        answer.append(r[0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))