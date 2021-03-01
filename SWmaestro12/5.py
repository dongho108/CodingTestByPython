def main():
    n = int(input())

    data = []
    max_time = 0
    for i in range(n):
        data.append(list(map(int, input().split())))
        for j in range(2, len(data[i])):
            if max_time < data[i][j]:
                max_time = data[i][j]

    time_graph = [[] for _ in range(max_time+1)]

    for i in range(len(data)):
        for j in range(2, len(data[i])):
            print(data[i][j], data[i][0])
            time_graph[data[i][j]].append(data[i][0])

    print(time_graph)



if __name__ == "__main__":
    main()