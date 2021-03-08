n = int(input())
t = [0] * n
p = [0] * n
dp = [0] * n

for i in range(n):
    t[i], p[i] = map(int, input().split())

max_value = 0

for i in range(n-1, -1, -1):
    if i+t[i] <= n-1:
        dp[i] = max(max_value, p[i]+dp[i+t[i]])
    else:
        if i+t[i] == n:
            dp[i] = max(max_value, p[i])
        else:
            dp[i] = max_value
    max_value = dp[i]


print(max_value)