n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

max_value = 0
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
        if i == n-1 and max_value < dp[i][j]:
            max_value = dp[i][j]

print(max_value)