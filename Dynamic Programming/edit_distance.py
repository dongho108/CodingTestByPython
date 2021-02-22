original_string = list(input())
new_string = list(input())

row_length = len(original_string)+1
col_length = len(new_string)+1

dp = [[5000] * (col_length) for _ in range(row_length)]


dp[0][0] = 0
for i in range(1, col_length):
    dp[0][i] = i

for i in range(1, row_length):
    dp[i][0] = i

for i in range(1, row_length): # i : ori
    for j in range(1, col_length): # j : new
        if original_string[i-1] == new_string[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

print(dp[row_length-1][col_length-1])
