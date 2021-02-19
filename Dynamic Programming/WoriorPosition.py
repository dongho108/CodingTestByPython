n = int(input())
data = list(map(int, input().split()))

d = [1 for _ in range(n)]

max_value = 0
for i in range(1, n):
    for j in range(0, i):
        if data[i] < data[j]:
            d[i] = max(d[i], d[j]+1)
    if max_value < d[i]:
        max_value = d[i]
if n == 1:
    print(0)
else:
    print(n - max_value)