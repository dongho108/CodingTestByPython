n = int(input())

data = []
for i in range(n):
    a, b, c, d = input().split()
    data.append((a, int(b), int(c), int(d)))

data.sort(key=lambda x:(((-x[1], x[2]), -x[3]), x[0]))

for i in range(n):
    print(data[i][0])