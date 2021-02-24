n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

max_value = 0
for i in range(n):
    if max_value < min(data[i]):
        max_value = min(data[i])

print(max_value)

'''
3 3
3 1 2
4 1 4
2 2 2
'''

'''
2 4
7 3 1 8
3 3 3 4
'''