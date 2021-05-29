#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, n, actions):

        data = [0] * (n+1)
        have = dict()
        for i in range(1, n+1):
            have[int(i)] = []

        for action in actions:
            action = list(action.split(" "))

            if action[0] == "PUT":
                i = int(action[1])
                j = int(action[3])
                if data[i] == 0 and data[j] == 0:
                    data[i] = j
                    have[j].append(i)
                else:
                    # print("1")
                    return -1
            elif action[0] == "SWAP":
                i = int(action[1])
                j = int(action[3])
                if data[i] == 0 and data[j] == 0:
                    tempA = []
                    tempB = []
                    for x in have[i]:
                        tempA.append(x)
                        data[x] = j
                    for x in have[j]:
                        tempB.append(x)
                        data[x] = i
                    have[i] = tempB
                    have[j] = tempA

                else:
                    # print("2")
                    return -1
            else:
                i = int(action[1])
                if data[i] == 0:
                    for x in have[i]:
                        data[x] = 0
                    have[i] = []
                else:
                    # print("3")
                    return -1

        # print(have)
        for i in have.keys():
            for j in have[i]:
                if j > i:
                    # print("4")
                    return -1

        count = -1
        for d in data:
            if d == 0:
                count += 1

        return count


print(Solution().solution(2, ["PUT 1 INSIDE 2"]))
# print(Solution().solution(2, ["PUT 1 INSIDE 2","SET 2 LOOSE"]))