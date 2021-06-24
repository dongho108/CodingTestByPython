n = int(input())

inp = []
for i in range(n):
    inp.append(list(map(int, input().split())))

data = [[0] * 100 for _ in range(100)]

for i in range(len(inp)):
    a, b = inp[i]
    for j in range(a, a+10):
        for k in range(b, b+10):
            data[j][k] = 1

# print(data)

answer = 0
for i in range(100):
    for j in range(100):
        if data[i][j] == 1:
            answer += 1
print(answer)