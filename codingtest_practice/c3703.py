n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)]

temp = 0
for i in range(n):
    temp += data[i][0]
    dp[i][0] = temp

temp = 0
for i in range(m):
    temp += data[0][i]
    dp[0][i] = temp


for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + data[i][j]

print(dp[n-1][m-1])