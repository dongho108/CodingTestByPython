n, target = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2

    length = 0
    for d in arr:
        if d >= mid:
            length += d - mid

    if length < target:
        end = mid-1
    else:
        result = mid
        start = mid + 1


print(result)
