n = int(input())
data = list(map(int, input().split()))
data.insert(0, 0)

d = [0 for _ in range(n+1)]
d[0] = data[0]
d[1] = data[1]
d[2] = data[2]

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2] + data[i])

print(d[n])