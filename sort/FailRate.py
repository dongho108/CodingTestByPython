def solution(N, stages):

    stages.sort()

    reachStageUser = 0  # 스테이지에 도달한 멤버
    clearStageUser = 0
    nowReachUserNum = [0 for _ in range(N+1)]  # 스테이지를 통과한 멤버

    stagesNum = len(stages)
    countStageNum = stagesNum+1

    answer = []
    failList = [[0, 0] for _ in range(N+1)]

    for i in range(stagesNum):
        countStageNum -= 1
        if i == 0:
            reachStageUser = 1
            nowReachUserNum[stages[i]] = countStageNum
            stagesNum -= 1
            continue


        if stages[i-1] != stages[i]:
            print(i)
            print(N, stages[i])
            if stages[i] <= N:
                nowReachUserNum[stages[i]] = countStageNum
            print(reachStageUser, nowReachUserNum[stages[i-1]])
            failList[stages[i-1]] = (stages[i-1], float(reachStageUser/nowReachUserNum[stages[i-1]]))
            reachStageUser = 1

        else:
            reachStageUser += 1
    print(failList)
    failList.sort(key=lambda x:(x[1], -x[0]), reverse=True)

    for f in failList:
        answer.append(f[0])

    answer.pop()
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))