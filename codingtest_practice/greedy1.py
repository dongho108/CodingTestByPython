n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]
count = 0
k_count = 0
result = 0

while count < m:
    if k_count == k:
        result += second
        k_count = 0
    else:
        result += first
        k_count += 1
    count += 1
print(result)