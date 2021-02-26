position = list(input())

# x = ord(position[0]) - 96
x = ord(position[0]) - ord('a') + 1
y = int(position[1])
print(x, y)
move = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]

count = 0
for m in move:
    if 0 < x+m[0] < 9 and 0 < y+m[1] <9:
        count += 1

print(count)
