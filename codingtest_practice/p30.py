from bisect import bisect_left
from bisect import bisect_right

def solution(words, queries):
    answer = []

    data = [[] for _ in range(10001)]
    data_reverse = [[] for _ in range(10001)]

    for word in words:
        length = len(word)
        data[length].append(word)
        data_reverse[length].append(word[::-1])

    for i in range(10001):
        data[i].sort()
        data_reverse[i].sort()

    for q in queries:
        start = q.replace("?", "a")
        end = q.replace("?", "z")
        l = len(q)

        query = list(q)
        if query[0] != "?":
            # 처음부터 비교
            left = bisect_left(data[l], start)
            right = bisect_right(data[l], end)
            answer.append(right-left)
        else:
            left = bisect_left(data_reverse[l], start[::-1])
            right = bisect_right(data_reverse[l], end[::-1])
            answer.append(right-left)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))