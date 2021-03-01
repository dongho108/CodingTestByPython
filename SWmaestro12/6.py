def main():
    n = int(input())
    data = list(map(int, input().split()))

    start = 0
    end = n-1

    # mid = (start + end) // 2
    # print(data[start : mid])

    value = 0
    while start != end:
        mid = (start + end) // 2
        left = max(data[start : mid+1])
        right = max(data[mid+1 : end+1])

        if left > right:
            start = mid+1
            value += left
        elif left < right:
            end = mid
            value += right
    print(value)


if __name__ == "__main__":
    main()