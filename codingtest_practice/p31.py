test = int(input())

for t in range(test):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    dp = []
    index = 0

    for i in range(n):
        dp.append(data[index:index+m])
        index += m

    result = 0
    for j in range(1, m):
        for i in range(n):
            max_value = 0
            for k in range(i-1, i+2):
                if 0 <= k < n:
                    if max_value < dp[k][j-1]:
                        max_value = dp[k][j-1]
            dp[i][j] = max_value+dp[i][j]
            if j == m - 1:
                if result < dp[i][j]:
                    result = dp[i][j]
    print(result)



'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''