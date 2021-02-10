n, m = map(int, input().split())

d = [10001 for _ in range(m+1)]
coin = []
for i in range(n):
    coin.append(int(input()))

for i in range(1, m+1):
    for c in coin:
        if d[i-c] < min_value and (i-c > 0):
            min_value = d[i-c]
    d[i] = min(min_value + 1, d[i])

print(d)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

