def solution(user_id, banned_id):
    answer = 0

    id_list = []
    for bid in banned_id:
        ids = []
        for uid in user_id:
            bid_l = list(bid)
            uid_l = list(uid)
            # print(bid, uid)
            if len(bid_l) == len(uid_l):
                match = True
                for i in range(len(bid_l)):
                    if bid_l[i] != '*':
                        if bid_l[i] != uid_l[i]:
                            match = False
                            break
                if match:
                    ids.append(uid)
        id_list.append(ids)



    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))