def binarySearch(data, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if data[mid] == target:
        return True
    elif data[mid] < target:
        return binarySearch(data, target, mid+1, end)
    else:
        return binarySearch(data, target, start, mid-1)


n = int(input())
data = list(map(int, input().split()))

m = int(input())
item = list(map(int, input().split()))

data.sort()
for i in range(m):
    if binarySearch(data, item[i], 0, n-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')

'''
5
8 3 7 9 2
3
5 7 9
'''