import math

def solution(w,h):
    answer = 1
    x = math.gcd(w, h)
    y = (w//x) + (h//x) - 1
    cross = x * y
    answer = w*h - cross
    return answer

print(solution(8, 12))