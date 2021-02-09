from bisect import bisect_left, bisect_right


def count_value(a, left, right):
    left_index = bisect_left(a, left)
    right_index = bisect_right(a, right)
    return right_index - left_index


def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]


    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_value(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_value(reverse_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))