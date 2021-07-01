from collections import deque


def differ(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            return False
    return count == 1


def solution(begin, target, words):
    answer = 0
    depth = 0

    words.insert(0, begin)
    visited = [False for _ in range(len(words))]

    q = deque()
    q.append((0, 0))

    while q:
        word_index, cost = q.popleft()
        print(words[word_index], cost)
        visited[word_index] = True

        if words[word_index] == target:
            result = cost
            break

        for i in range(len(words)):
            if not visited[i] and differ(words[word_index], words[i]):
                q.append((i, cost + 1))

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))



