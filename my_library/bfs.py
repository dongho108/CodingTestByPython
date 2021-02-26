from collections import deque

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input())))

q = deque()
q.append((0, 0, 1))
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = 0
while q:
    x, y, cost = q.popleft()
    if x == n-1 and y == m-1:
        result = cost
        break

    for d in dir:
        nx = x+d[0]
        ny = y+d[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if data[nx][ny] == 1:
            q.append((nx, ny, cost+1))

print(cost)

'''
5 6
101010
111111
000001
111111
111111
'''