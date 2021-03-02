from collections import deque

def main():
    n = int(input())

    data = []
    max_time = 0
    for i in range(n*n):
        data.append(list(map(int, input().split())))
        for j in range(2, len(data[i])):
            if max_time < data[i][j]:
                max_time = data[i][j]

    time_graph = [[] for _ in range(max_time+1)]

    for i in range(len(data)):
        for j in range(2, len(data[i])):
            time_graph[data[i][j]].append(data[i][0])

    result = 0
    for i in range(1, len(time_graph)):
        result += max(time_graph[i])

    print(result)



if __name__ == "__main__":
    main()


'''
2
1 3 1 3 5
2 2 2 4
3 2 1 2
4 1 3
'''
