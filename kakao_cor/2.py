from itertools import combinations

def solution(needs, r):
    answer = 0
    comb = list(combinations(range(len(needs[0])), r))

    max_value = 0
    for c in comb:
        count = 0
        for i in range(len(needs)):
            test = []
            for j in range(len(needs[0])):
                if needs[i][j] == 1:
                    test.append(j)

            t_count = 0
            for t in test:
                if t in c:
                    t_count += 1
            if t_count == len(test):
                count += 1

        if max_value < count:
            max_value = count
    answer = max_value

    return answer


print(solution([ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ], 2))