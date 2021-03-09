def main():
    n = int(input())
    result = dict()
    for i in range(n*n):
        data = list(map(int, input().split()))
        s = data[0]
        k = data[1]
        t = data[2:]

        for j in range(k):
            if t[j] in result:
                result[t[j]] = max(result[t[j]], s)
            else:
                result[t[j]] = s

    print(sum(result.values()))


if __name__ == "__main__":
    main()


'''
2
1 3 1 3 5
2 2 2 4
3 2 1 2
4 1 3
'''
