import re

def cal_left(words, length, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if len(words[mid]) == length and (mid == 0 or len(words[mid-1]) < length):
        return mid
    elif length <= len(words[mid]):
        return cal_left(words, length, start, mid-1)
    else:
        return cal_left(words, length, mid+1, end)


def cal_right(words, length, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if len(words[mid]) == length and (mid == len(words)-1 or len(words[mid+1]) > length):
        return mid
    elif length < len(words[mid]):
        return cal_right(words, length, start, mid-1)
    else:
        return cal_right(words, length, mid+1, end)




def count_value(query, length, words):
    n = len(words)
    left_index = cal_left(words, length, 0, n-1)
    if left_index is None:
        return 0

    right_index = cal_right(words, length, 0, n-1)
    count = 0

    query = query.replace("?", ".")
    p = re.compile(query)

    for i in range(left_index, right_index+1):
        if p.match(words[i]) is not None:
            count += 1
    return count



def solution(words, queries):
    answer = []

    words.sort(key=lambda x:len(x))

    for q in queries:
        length = len(q)
        answer.append(count_value(q, length, words))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))