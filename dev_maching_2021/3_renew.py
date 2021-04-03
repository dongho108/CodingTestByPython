def solution(enroll, referral, seller, amount):
    answer = []

    new_enroll = ["center"]
    for i in enroll:
        new_enroll.append(i)

    new_referral = [""]
    for i in referral:
        new_referral.append(i)

    n = len(new_enroll)
    graph = [-1] * (n)
    bfs_graph = [[] for _ in range(n)]

    for i in range(len(new_referral)):
        # i 는 refferal의 인덱스 = enroll의 사람 순서
        ref = new_referral[i]

        if ref == "":
            continue
        # 추천인이 없다면 민호(center)(graph상 첫번째 인덱스)와 연결
        if ref == "-":
            graph[i] = 0
            bfs_graph[0].append(i)
        else:
            up_index = new_enroll.index(ref)
            graph[i] = up_index
            bfs_graph[up_index].append(i)

    print(new_enroll)
    print(graph)
    enroll_cost = [0] * (n)
    print(enroll_cost)

    for i in range(len(seller)):
        cost = amount[i] * 100
        pre_index = new_enroll.index(seller[i])
        enroll_cost[pre_index] += (cost * 0.9)

        now = cost * 0.1
        print(pre_index)
        while True:
            now_index = graph[pre_index]

            print(now_index, now)
            if now_index == -1:
                break

            if now * 0.1 > 1:
                enroll_cost[now_index] += now * 0.9
                now = now * 0.1
                print(now)
                pre_index = now_index
            else:
                if now < 2:
                    enroll_cost[now_index] = 1
                else:
                    enroll_cost[now_index] += now
                break

        print(enroll_cost)
    answer = enroll_cost
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
# 입출력 예
# enroll	referral	seller	amount	result
# ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["young", "john", "tod", "emily", "mary"]	[12, 4, 2, 5, 10]	[360, 958, 108, 0, 450, 18, 180, 1080]
# ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["sam", "emily", "jaimie", "edward"]	[2, 3, 5, 4]	[0, 110, 378, 180, 270, 450, 0, 0]
