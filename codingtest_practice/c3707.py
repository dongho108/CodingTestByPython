n = int(input())
dp = [0] * (n+1)

dp[1]=1

for i in range(2, n+1):
    x = 0
    for j in range(1, i):
        x += (dp[j] * dp[i-j])
    dp[i] = x

print(dp)
print(dp[n])