a, b = map(int, input().split())

i = 0
count = 0
data = []
while count < b:
    for j in range(i+1):
        data.append(i+1)
        count += 1
    i += 1

# print(data[a-1:b])
print(sum(data[a-1:b]))