from itertools import permutations

def solution(n, weak, dist):
    answer = 0

    length = len(weak)
    for i in range(length):
        weak.append(n+weak[i])


    answer = len(dist) + 1
    for start in range(length):  # 취약점들을 시작점으로 두려고
        for friends in list(permutations(dist, len(dist))):  # 모든 경우의 친구들 순서
            count = 1
            position = weak[start] + friends[count-1]

            for index in range(start, start + length):  # 친구 늘릴떄마다 다음 취약점 자리 구하려고
                if position < weak[index]:  # 갈 수 있는 범위 < 현재 타겟 취약점
                    count += 1  # 친구 한명 더 필요
                    if count > len(dist):  # 더이상 친구 없으면 끝
                        break
                    # 친구 한명 더 늘린만큼 범위 넓어짐
                    # 다음 취약점에서부터 그 추가된 친구의 범위만큼 커짐
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)

    if answer > len(dist):  # answer이 처음이랑 똑같음 (친구 다 해도 커버못함)
        return -1

    return answer


print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))