def slice_dduk(dList, mid):
    sum = 0
    for d in dList:
        if d >= mid:
            sum += d - mid
    return sum


def binary_search(data, target, start, end, nowans):
    if start > end:
        return nowans

    mid = (start + end) // 2
    length = slice_dduk(data, mid)
    print(data, mid, length)

    if length == target:
        return mid
    elif length < target:
        return binary_search(data, target, start, mid-1, nowans)
    else:
        return binary_search(data, target, mid+1, end, mid)


n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, max(arr), 0)
print(result)
