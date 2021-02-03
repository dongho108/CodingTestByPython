import heapq

n = int(input())
data = []
for i in range(n):
    heapq.heappush(data, int(input()))

result = 0
while True:
    if len(data) == 1:
        break
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    result += a+b
    heapq.heappush(data, a+b)


print(result)


