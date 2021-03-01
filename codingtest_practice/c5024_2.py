n, c = map(int, input().split())
data = []

for i in range(n):
    a = int(input())
    data.append(a)

data.sort()

start = data[0]
end = data[-1]

result = 0
while start <= end:
    mid = (start + end) // 2
    target = data[0]
    count = 1
    for i in range(1, n):
        if data[i] >= target + mid:
            target = data[i]
            count += 1

    if count < c: # 갭 줄이기
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)

