from itertools import combinations

def solution(orders, course):
    answer = []

    count = dict()
    max_cource = [[] for _ in range(11)]
    len_word_list = [[] for _ in range(21)]

    # # for c in course: # 10
    for order in orders: # 20
        for i in range(len(order)-1): # 10-2 = 8
            for j in range(i+1, len(order)): # 10-1 = 9
                comb = order[i:j+1]
                length = len(comb)

                print(length, comb)

                len_word_list[length].append(comb)

                if comb in count:
                    count[comb] += 1
                else:
                    count[comb] = 1
    
    for c in course:
        len_word_set = set(len_word_list[c])
        len_word_list[c] = list(len_word_set)
        print(len_word_list[c])
        max_value = 0

        for word in len_word_list[c]:
            if max_value < int(count[word]):
                max_value = int(count[word])

        # test
        for word in len_word_list[c]:
            print(word, count[word])

        if max_value < 2:
            continue

        for word in len_word_list[c]:
            if count[word] == max_value:
                answer.append(word)


    answer.sort()
    return answer


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))