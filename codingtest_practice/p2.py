data = list(map(int, input()))

result = data[0]
for i in range(1, len(data)):
    if data[i-1] == 0:
        result += data[i]
    else:
        result *= data[i]

print(result)
