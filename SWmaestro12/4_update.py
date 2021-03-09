def main():
    n = int(input())
    data = list(map(int, input().split()))

    max_value = 0
    for i in range(3):
        visited = [False] * n
        count = 0
        now = i
        while True:
            count += 1
            if visited[now] == True:
                break
            visited[now] = True
            now += data[now]

        if max_value < count:
            max_value = count

    print(max_value)


if __name__ == "__main__":
    main()

'''
10
3 5 -1 -2 4 4 3 -2 -3 -2
'''