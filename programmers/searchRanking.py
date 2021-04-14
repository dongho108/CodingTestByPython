from bisect import bisect_left

def solution(info, query):
    answer = []

    info_dict = dict()
    score = [0] * len(info)

    for i in range(len(info)):
        info_list = info[i].split(" ")
        for j in range(len(info_list)):
            if j == len(info_list) - 1:
                score[i] = info_list[j]
                continue

            if info_list[j] not in info_dict:
                info_dict[info_list[j]] = []
                info_dict[info_list[j]].append(score[i])
            else:
                info_dict[info_list[j]].append(score[i])

    # print(info_dict)
    # print(score)

    for i in range(len(query)):
        q_split = query[i].split(" ")
        while "and" in q_split:
            q_split.remove("and")
        # print(q_split)

        if q_split[0] == "-":
            temp = [x for x in range(len(info))]
        else:
            temp = info_dict[q_split[0]]

        # print(temp)
        for j in range(1, len(q_split)-1):
            if q_split[j] == "-":
                continue
            temp = list(set(temp).intersection(info_dict[q_split[j]]))
            # print(temp)

        count = 0
        for t in temp:
            if int(q_split[-1]) <= int(score[t]):
                count += 1
        answer.append(count)

    return answer

print((solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])))