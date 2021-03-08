n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()
start = 1
end = data[-1] - data[0]

result = 0
while start <= end:
    mid = (start+end) // 2

    count = 1
    now = data[0]
    for i in range(1, n):
        if now + mid <= data[i]:
            now = data[i]
            count += 1

    if count < c:
        end = mid-1
    elif count >= c:
        result = mid
        start = mid+1

print(result)