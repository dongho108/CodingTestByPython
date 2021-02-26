n = int(input())
coin = list(map(int, input().split()))

coin.sort()

target = 1

for c in coin:
    if target < c:
        print(target)
        break
    target += c
