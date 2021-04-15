def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())

visited = [False] * (g+1)
visited[0] = True
parent = [i for i in range(g+1)]
count = 0

for i in range(p):
    data = int(input())

    # pa : 입력된 gi의 루트
    pa = find_parent(parent, data)

    # 루트가 방문되어잇지 않다면 루트에 도킹
    if not visited[pa]:
        visited[pa] = True
        count += 1

        # 도킹 : 해당 탑승구를 바로 아래 탑승구를 가리키게함
        union(parent, pa, pa-1)
    else:
        break

# print(parent)

print(count)

'''
4
3
4
1
1

4
4
4
3
2
1
'''