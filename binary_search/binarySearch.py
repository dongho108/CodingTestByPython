def binary_search(data, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search(data, target, start, mid-1)
    else:
        return binary_search(data, target, mid+1, end)




n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("X")
else:
    print(result + 1)