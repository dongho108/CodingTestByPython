import heapq


def solution(jobs):
    answer = 0

    jobs.sort(key=lambda x: x[0])

    time = jobs[0][1]
    index = 0
    q = []

    count = 0
    now_time = jobs[0][0]
    next_time = jobs[0][0] + time
    ptr = 1
    work = True

    while count < len(jobs):

        # 매 시간마다 작업 큐에 대기작업 넣기
        first_check = False
        if ptr
        while now_time == jobs[ptr][0]:
            if not first_check:
                next_time = now_time + jobs[ptr][1]
                first_check = True
            heapq.heappush(q, (jobs[ptr][1], ptr))
            ptr += 1
            if ptr == len(jobs):
                break

        # 작업끝나는 시간에 answer, count 업데이트
        if now_time == next_time:
            answer += (now_time - jobs[index][0])
            count += 1
            work = False

        # 작업중이 아닐때 작업큐에서 작업 꺼내기
        if not work:
            time, index = heapq.heappop(q)
            next_time = now_time + time
            work = True

        now_time += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]	))