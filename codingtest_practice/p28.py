n = int(input())
data = list(map(int, input().split()))

start = 0
end = len(data)-1

result = -1
while start <= end:
    mid = (start + end) // 2

    if mid == data[mid]:
        result = mid
        break
    elif mid > data[mid]:
        start = mid+1
    else:
        end = mid-1

print(result)

'''
5
-15 -6 1 3 7

7
-15 -4 3 8 9 13 15
'''