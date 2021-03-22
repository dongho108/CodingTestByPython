def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
    print("=====")


n, m = map(int, input().split())

INF = int(1e9)
dp = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dp[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

result = 0

# display(dp)
for j in range(1, n+1):
    count = 0
    for i in range(1, n+1):
        if i == j:
            continue
        if dp[i][j] != INF or dp[j][i] != INF:
            count += 1
    # print(i, j, count)
    if count == n-1:
        result += 1

print(result)

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''