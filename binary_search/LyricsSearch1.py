import re


def count_value(query, length, wordList):
    count = 0
    query = query.replace("?", ".")
    p = re.compile(query)

    for w in wordList:
        if p.match(w) is not None:
            count += 1
    return count


def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)

    for i in range(10001):
        array[i].sort()

    for q in queries:
        length = len(q)
        answer.append(count_value(q, length, array[length]))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))