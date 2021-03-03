from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

left = bisect_left(data, x)
right = bisect_right(data, x)

result = right - left

if result == 0:
    print(-1)
else:
    print(right-left)

'''
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''