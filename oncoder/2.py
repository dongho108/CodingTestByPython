#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, X, Y, walkTime, sneakTime):
        answer = 0
        if walkTime*2 < sneakTime:
            answer = walkTime * (X+Y)
        else:
            sneak = min(X, Y)
            X = X - sneak
            Y = Y - sneak

            rest = max(X, Y)
            answer = sneak * sneakTime
            if sneakTime < walkTime:
                answer += (rest//2) * (sneakTime*2)
                rest %= 2

            answer += rest * walkTime

        return answer


print(Solution().solution(4, 2, 3, 5))
print(Solution().solution(2, 0, 12, 10))
print(Solution().solution(2, 4, 12, 10))
print(Solution().solution(2, 5, 12, 10))
# print(Solution().solution(1000000000, 1000000000, 10000, 10000))