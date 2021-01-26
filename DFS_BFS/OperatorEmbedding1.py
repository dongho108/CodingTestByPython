def dfs(i, pre):
    global add, sub, mul, div, min_value, max_value

    if i == n:
        results.append(pre)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, pre + data[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i + 1, pre - data[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i + 1, pre * data[i])
            mul += 1

        if div > 0:
            div -= 1
            if pre < 0 and data[i] > 0:
                pre = abs(pre)
                dfs(i + 1, -(pre // data[i]))
            else:
                dfs(i + 1, pre // data[i])
            div += 1


n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

results = []

dfs(1, data[0])


print(max(results))
print(min(results))