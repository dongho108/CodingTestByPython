n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()

card = data[0]
answer = []

for i in range(1, n):
    card += data[i]
    answer.append(card)

print(sum(answer))
