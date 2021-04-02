def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    t, a, b = map(int, input().split())

    if t == 0:
        union(a, b)
    elif t == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")


'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''

