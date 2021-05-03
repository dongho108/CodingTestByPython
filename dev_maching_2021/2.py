def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end='\t')
        print()
    print("=====")


def solution(rows, columns, queries):
    answer = []

    graph = []
    data = 0

    for i in range(rows):
        temp = []
        for j in range(columns):
            data += 1
            temp.append(data)
        graph.append(temp)

    display(graph)


    temp_graph = [[0] * columns for _ in range(rows) ]

    for i in range(rows):
        for j in range(columns):
            temp_graph[i][j] = graph[i][j]


    n = queries[0][2] - queries[0][0] + 1 + queries[0][0]
    m = queries[0][3] - queries[0][1] + 1 + queries[0][1]
    print(n, m)

    for i in range(queries[0][0], queries[0][2]+1):
        for j in range(queries[0][1], queries[0][3]+1):
            temp_graph[i][j] = temp_graph[n-1-j][i]
            print(n-1-j, i)
            print(temp_graph[i][j], " -> ", temp_graph[n-1-j][i])

    display(temp_graph)


    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# 입출력 예시
# rows	columns	queries	result
# 6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
# 3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
# 100	97	[[1,1,100,97]]	[1]