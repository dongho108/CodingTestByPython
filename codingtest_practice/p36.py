row = list(input())
column = list(input())

dp = [[0] * (len(column)+1) for _ in range(len(row)+1)]

for i in range(len(row)+1):
    dp[i][0] = i

for i in range(len(column) + 1):
    dp[0][i] = i

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        a = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        if row[i-1] == column[j-1]:
            dp[i][j] = a
        else:
            dp[i][j] = a+1

print(dp[len(row)][len(column)])

'''
cat
cut

sunday
saturday
'''