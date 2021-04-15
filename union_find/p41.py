def find_parent(parent, x):
    if x != parent[x]:
        return find_parent(parent, parent[x])
    return x


def union(parent, a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [i for i in range(n)]

for i in range(n):
    data = list(map(int, input().split()))

    for j in range(len(data)):
        if data[j] == 1:
            print(find_parent(parent, i), find_parent(parent, j))
            if find_parent(parent, i) != find_parent(parent, j):
                union(parent, i, j)

course = list(map(int, input().split()))
set_course = set(course)
course = list(set_course)

pa = parent[course[0]]

print(parent)

answer = False
for i in range(1, len(course)):
    if parent[course[i]] == pa:
        answer = True
    else:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")

'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3


5 4
0 1 0 0 0
1 0 0 0 0
0 0 0 1 1
0 0 1 0 0 
0 0 1 0 0
2 3 4 3
'''