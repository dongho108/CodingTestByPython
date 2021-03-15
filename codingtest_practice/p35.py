import heapq

n = int(input())

answer = []
data = []
data.append(1)

while len(answer) < n:
    target = heapq.heappop(data)
    a = [0]*3
    a[0], a[1], a[2] = target*2, target*3, target*5

    for i in a:
        if i not in data:
            heapq.heappush(data, i)

    answer.append(target)

print(answer[-1])