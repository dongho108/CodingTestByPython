import heapq


def solution(jobs):
    answer = 0

    jobs.sort(key=lambda x: (x[0],x[1]))

    wait = sorted(jobs, key=lambda x:x[0])

    start, time = wait.pop(0)
    now = start
    finish = start + time
    q = []
    count = 0
    work = True

    while count < len(jobs):

        if wait:
            while now == wait[0][0]:
                w_start, w_time = wait.pop(0)
                heapq.heappush(q, (w_time, w_start))
                if not wait:
                    break

        if now == finish:
            answer += (now - start)
            count += 1
            work = False

        if not work:
            if q:
                time, start = heapq.heappop(q)
                finish = now + time
                work = True

        now += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 3], [6, 4], [7, 5]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))


#  jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
#  result = 72