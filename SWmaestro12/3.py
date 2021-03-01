def main():
    n, m, e = map(int, input().split())

    data = list(map(int, input().split()))
    length = data[-1]
    graph = [0] * (length+1)

    for d in data:
        graph[d] = 1

    if graph[e] == 1:
        count = 1
    else:
        count = 0

    i = e+1
    j = e-1
    a = 0
    b = 0
    while count < m:
        if graph[i] == 1:
            a = i
            count += 1
        if graph[j] == 1:
            b = j
            count += 1

        i += 1
        j -= 1

    result = abs(a-e) + abs(b-e)
    print(result)



if __name__ == "__main__":
    main()