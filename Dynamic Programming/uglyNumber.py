def agly_number(x):
    if x == 1:
        return 1

    if x % 2 == 0:
        if dp[x//2] == 1:
            return 1
        else:
            return agly_number(x // 2)
    elif x % 3 == 0:
        if dp[x // 3] == 1:
            return 1
        else:
            return agly_number(x // 3)
    elif x % 5 == 0:
        if dp[x // 5] == 1:
            return 1
        else:
            return agly_number(x // 5)
    else:
        return 0


n = int(input())

dp = [0]*1000000
dp[1] = 1

count = 1
i = 2

while count < n:
    dp[i] = agly_number(i)
    if dp[i] == 1:
        count += 1
    # print(dp[i], i)
    i += 1

print(i-1)