n, m = map(int, input().split())
data = list(map(int, input().split()))

start = min(data)
end = max(data)

result = -1
while start <= end:
    mid = (start + end) // 2

    length = 0
    for i in range(n):
        if data[i] > mid:
            length += (data[i] - mid)

    if length >= m:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)

'''
4 6
19 15 10 17
'''
