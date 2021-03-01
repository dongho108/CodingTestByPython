from itertools import combinations

n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

batch = list(combinations(data, c))

# print(batch)

max_value = 0
for bat in batch:
    bat = list(bat)
    bat.sort()


    min_gap = int(1e9)
    for bi in range(1, c):
        gap = bat[bi] - bat[bi-1]
        if min_gap > gap:
            min_gap = gap
    if max_value < min_gap:
        max_value = min_gap

print(max_value)