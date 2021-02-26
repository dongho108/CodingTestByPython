from itertools import combinations

n = int(input())
coin = list(map(int, input().split()))

data = [0] * sum(coin) * n

for i in range(1, n+1):
    comb = list(combinations(coin, i))
    for j in comb:
        data[sum(j)] = 1


for i in range(1, len(data)+1):
    if data[i] == 0:
        print(i)
        break
