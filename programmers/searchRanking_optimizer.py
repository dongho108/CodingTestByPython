from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = dict()

    # info 의 모든 조합으로 dict 만들기
    for i in range(len(info)):
        info_split = info[i].split(" ")
        str_list = []

        score = int(info_split.pop())

        # 16개의 조합을 만들땐 스택(큐)을 이용한다.
        # 지금까지 만든 조합들 모두를 꺼내면서 해당 자리에 단어를 넣거나, "-"를 넣는 두가지를 만들어서 다시 집어넣는다.

        # 초기에 첫단어와 "-" 넣기
        str_list.append(info_split[0])
        str_list.append("-")

        for j in range(1, len(info_split)):
            length = len(str_list)

            # 현재 존재하는 조합의 개수만큼 다음 단어를 넣거나 "-"를 넣는 두가지를 만들어서 다시 집어넣는다.
            for _ in range(length):
                temp = str_list.pop(0)
                str_list.append(temp+info_split[j])
                str_list.append(temp+"-")

        for st in str_list:
            if st not in info_dict:
                info_dict[st] = []
                info_dict[st].append(score)
            else:
                info_dict[st].append(score)

    # dict의 score들을 정렬하기
    for idk in info_dict.keys():
        info_dict[idk].sort()

    # 모든 query에 대해서 점수를 구하고 그 점수 이상인 조합들의 개수를 구한다.
    for i in range(len(query)):
        q_split = query[i].replace('and', '').split(" ")

        # print(q_split)
        temp_str = ""
        score = int(q_split.pop())

        for j in range(len(q_split)):
            temp_str += q_split[j]

        if temp_str not in info_dict:
            answer.append(0)
            continue
        else:
            score_list = info_dict[temp_str]

        left_index = bisect_left(score_list, score)

        # print(score_list)
        # print(score, len(score_list) - left_index)
        
        answer.append(len(score_list) - left_index)

    return answer

# print((solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])))
# print((solution(["java backend junior pizza 50"], ["python and - and - and - 50"])))