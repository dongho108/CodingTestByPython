import heapq


def solution(operations):
    answer = []

    q = []

    for operation in operations:
        op, n = operation.split()
        print(q)
        if op == "I":
            heapq.heappush(q, n)
        else:
            if not q:
                continue
            if n == "1":
                q.pop()
            else:
                heapq.heappop(q)

    if q:
        if len(q) == 1:
            tmp = q.pop()
            answer.append(tmp)
            answer.append(tmp)
        else:
            answer.append(q.pop())
            answer.append(heapq.heappop(q))
    else:
        answer.append(0)
        answer.append(0)

    return answer