from itertools import permutations


def isMatch(cid, bid):
    # print(cid, bid)
    for i in range(len(cid)):
        if bid[i] != '*':
            if bid[i] != cid[i]:
                return False
    return True


def check(c_id, banned_id):
    # print(c_id, banned_id)
    # print(len(c_id[0]), banned_id[0])
    for i in range(len(c_id)):
        if len(c_id[i]) != len(banned_id[i]):
            return False
        else:
            if not isMatch(list(c_id[i]), list(banned_id[i])):
                return False
    return True


def solution(user_id, banned_id):
    answer = 0

    result_set = set()

    for c_id in list(permutations(user_id, len(banned_id))):
        if check(c_id, banned_id):
            result_set.add(''.join(sorted(c_id)))

    print(result_set)
    answer = len(result_set)

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))