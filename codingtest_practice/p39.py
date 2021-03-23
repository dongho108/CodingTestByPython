import heapq


def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()
    print("=====")


t = int(input())


while t > 0:

    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    INF = int(1e9)
    distance = [[INF]*n for i in range(n)]

    q = []
    q.append((data[0][0], 0, 0))
    distance[0][0] = data[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for d in dir:
            nx = d[0] + x
            ny = d[1] + y

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + data[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    display(distance)
    print(distance[n-1][n-1])


    t -= 1

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 8 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''