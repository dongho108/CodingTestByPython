def first(data, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target and (mid == 0 or data[mid-1] < target):
        return mid
    elif target <= data[mid]:
        return first(data, target, start, mid-1)
    else:
        return first(data, target, mid+1, end)


def last(data, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if data[mid] == target and (mid == n-1 or data[mid+1] > target):
        return mid
    elif target < data[mid]:
        return last(data, target, start, mid-1)
    else:
        return last(data, target, mid+1, end)


def count_by_value(data, target):
    left = first(data, target, 0, n-1)
    if left == None:
        return 0

    right = last(data, target, 0, n-1)
    return right-left+1


n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = count_by_value(arr, x)

if result == 0:
    print(-1)
else:
    print(result)
