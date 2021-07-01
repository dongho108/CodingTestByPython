import heapq


def solution(tickets):
    answer = []

    paths = dict()

    for i in range(len(tickets)):
        a, b = tickets[i]
        if paths.get(a) is None:
            paths[a] = list()
        heapq.heappush(paths[a], b)

    q = ["ICN"]

    while q:
        print(q)
        start = q[-1]

        if paths.get(start) is None:
            answer.append(q.pop())
        else:
            q.append(heapq.heappop(paths[start]))

    answer.reverse()

    return answer

print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))


# T 1 : [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# ans : ["ICN", "B", "ICN", "A", "D", "A"]
#
# T 2: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
# ans : ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
#
# T 3 : [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
# ans : ["ICN", "COO", "ICN", "BOO", "DOO"]
#
# 4번 반례 해결하니 2번 테케 통과했습니다.
# T 4: [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
# ans : ["ICN", "SFO", "ICN", "SFO", "QRE"]
#
# 가장 골치아픈 1번테케는 5번반례 해결후 통과했습니다.
# T 5 : [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# ans : ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]