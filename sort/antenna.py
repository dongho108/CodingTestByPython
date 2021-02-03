import sys


def dist(x, data):
    sum = 0
    for d in data:
        # print(f"|{x} - {d}| = {abs(x-d)}")
        sum += abs(x-d)
    # print(sum)
    return sum


n = int(input())
data = list(map(int, input().split()))

length = max(data)

min_value = sys.maxsize
result = -1
for i in range(1, length+1):
    temp = dist(i, data)
    if temp < min_value:
        min_value = temp
        result = i

print(result)
