def display(d):
    for i in range(len(d)):
        for j in range(len(d[0])):
            print(d[i][j], end='  ')
        print()


tc = int(input())
for t in range(tc):
    n, m = map(int, input().split())
    temp_data_list = list(map(int, input().split()))
    temp_count = 0
    data = [[0] * (m+1) for _ in range(n+2)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            data[i][j] = temp_data_list[temp_count]
            temp_count += 1

    d = [[0] * (m+1) for _ in range(n+2)]

    d[1][1] = data[1][1]
    d[2][1] = data[2][1]
    d[3][1] = data[3][1]
    maxList = []
    for j in range(2, m+1):
        for i in range(1, n+1):
            d[i][j] = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1]) + data[i][j]
            if j == m:
                maxList.append(d[i][j])
    display(d)
    print(max(maxList))


'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''