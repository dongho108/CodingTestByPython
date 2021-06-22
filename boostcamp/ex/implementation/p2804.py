a, b = input().split()

a = list(a)
b = list(b)

# count = [len(a), len(b)]

point_check = False
a_point = -1
b_point = -1
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a_point = i
            b_point = j
            point_check = True
            break
    if point_check:
        break

a_count = 0
b_count = 0

for i in range(len(b)):
    for j in range(len(a)):

        if i == b_point and j == a_point:
            print(a[a_count], end="")
            a_count += 1
            b_count += 1
            continue

        if i == b_point:
            print(a[a_count], end="")
            a_count += 1
        elif j == a_point:
            print(b[b_count], end="")
            b_count += 1
        else:
            print(".", end="")
    print()