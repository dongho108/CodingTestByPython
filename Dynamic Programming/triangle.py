n = int(input())
data = []

for i in range(n):
    data.append(list(map(int ,input().split())))

d = [[0] * n for _ in range(n)]

d[0][0] = data[0][0]
for i in range(n):
    for j in range(i+1):
        if j-1 < 0:
            d[i][j] = d[i-1][j] + data[i][j]
        elif i == j:
            d[i][j] = d[i-1][j-1] + data[i][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-1]) + data[i][j]
# print(d)
print(max(d[n-1]))
