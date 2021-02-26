from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

comb = list(combinations(data, 2))

count = 0
for c in comb:
    if c[0] == c[1]:
        count += 1

print(len(comb) - count)