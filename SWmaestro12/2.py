def main():
    p, n, h = map(int, input().split())

    pc = [h] * (p+1)


    for i in range(n):
        a, b = map(int, input().split())
        if pc[a] < b:
            continue
        pc[a] -= b

    for i in range(1, p+1):
        cost = (h - pc[i]) * 1000
        print(i, cost)


if __name__ == "__main__":
    main()