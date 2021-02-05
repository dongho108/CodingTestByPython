from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))


def count_by_range(a, left, right):
    left_index = bisect_left(a, left)
    right_index = bisect_right(a, right)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4 ,4 ,8, 9]
print(count_by_range(a, 4, 9))
print(count_by_range(a, -1, 9))
