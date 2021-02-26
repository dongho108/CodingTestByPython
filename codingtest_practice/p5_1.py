n, m = map(int, input().split())
data = list(map(int, input().split()))

arr = [0] * 11

for d in data:
    arr[d] += 1


result = 0
length = len(data)
for i in range(1, m+1):
    result += arr[i] * (length - arr[i])
    length -= arr[i]

print(result)
