n, m = map(int, input().split())

d = [10001 for _ in range(10001)]
coin = []
for i in range(1, n+1):
    temp = int(input())
    d[temp] = 1
    coin.append(temp)

for i in range(1, m+1):
    min_value = 10001
    for c in coin:
        if d[i-c] < min_value and (i-c > 0):
            min_value = d[i-c]
    d[i] = min(min_value + 1, d[i])

print(d)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

