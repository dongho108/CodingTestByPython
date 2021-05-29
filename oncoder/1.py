#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, price, cost):
        answer = 0
        max_result = 0
        for now in price:
            now_result = 0
            for i in range(len(price)):
                if price[i] >= now >= cost[i]:
                    now_result += (now-cost[i])
            # print(now_result)
            if max_result < now_result:
                max_result = now_result
                answer = now
        return answer

# print(solution([13,22,35], [5,15,30]))
# print(solution([10,10,20,20,5], [1,5,11,15,0]))

# print(Solution.solution([13,22,35], [15,30,40]))

print(Solution().solution([13,22,35], [5,15,30]))
print(Solution().solution(price=[13,22,35], cost=[15,30,40]))