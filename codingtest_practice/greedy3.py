n, k = map(int, input().split())

count = 0
while k <= n:
    n = n // k
    count += 1

while n != 1:
    n -= 1
    count += 1

print(count)