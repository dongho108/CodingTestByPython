n = int(input())
data = [[0] for _ in range(n)]

print(data)

for i in range(n):
    t, p = map(int, input().split())
    index = i + (t-1)
    print(index)
    if index >= n:
        continue
    else:
        data[index].append(p)
print(data)
result = 0
for i in range(n):
    result += max(data[i])
    print(i, result)
print(result)
