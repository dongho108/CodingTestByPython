n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()
start = 1
end = data[-1] - data[0]

result = 0
while start <= end:
    gap = (start + end) // 2
    print(f"gap = {gap}")
    count = 1

    temp = data[0]+gap
    for i in range(1, n):
        if temp <= data[i]:
            print(f"temp, data[{i}] = {temp}, {data[i]}")
            count += 1
            temp = data[i] + gap
    print(f"count = {count}")

    if count >= c:
        start = gap + 1
        result = gap
    else:
        end = gap - 1

print(result)

