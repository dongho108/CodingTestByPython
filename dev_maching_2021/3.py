def solution(enroll, referral, seller, amount):
    answer = []

    bfs_graph = [[] for _ in range(len(enroll)+1)]
    graph = [[] for _ in range(len(enroll)+1)]

    graph[-1].append(-1)
    for i in range(len(referral)):
        # i 는 refferal의 인덱스 = enroll의 사람 순서

        ref = referral[i]

        # 추천인이 없다면 민호(center)(graph상 마지막 인덱스)와 연결
        if ref == "-":
            graph[i].append(-1)
            bfs_graph[-1].append(i)
        else:
            up_index = enroll.index(ref)
            graph[i].append(up_index)
            bfs_graph[up_index].append(i)

    print(graph)
    print(bfs_graph)
    enroll_cost = [0] * (len(enroll)+1)

    for i in range(len(seller)):
        now_seller = enroll.index(seller[i]) # young, 7
        up_index = graph[now_seller][0] # 2

        print(now_seller, up_index)
        cost = amount[i] * 1000

        while True:
            now_cost =
            if up_index == -1:
                if cost * 0.1 > 1:
                    upcost = cost * 0.1
                    mycost = cost * 0.9
                else:
                    mycost = cost
                    upcost = 0

                break
            if cost * 0.1 > 1:
                upcost = cost * 0.1
                mycost = cost * 0.9
            else:
                mycost = cost
                upcost = 0

            print(up_index)
            enroll_cost[now_seller] += mycost
            enroll_cost[up_index] += upcost
            now_seller = up_index
            up_index = graph[now_seller][0]
        print(enroll_cost)


    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
