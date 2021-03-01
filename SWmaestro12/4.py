def main():
    n = int(input())
    data = list(map(int, input().split()))

    max_value = 0
    for i in range(3):
        # print('===========')
        visited = [False] * n
        count = 1
        visited[i] = True
        now = data[i]

        while visited[now] != True:
            visited[now] = True
            count += 1
            # print(count)
            # print(now, data[now], now+data[now])
            # print(visited)
            now = now + data[now]

        count += 1
        if max_value < count:
            max_value = count

    print(max_value)


if __name__ == "__main__":
    main()