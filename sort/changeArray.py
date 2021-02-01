n, k = map(int, input().split())
array_A = []
array_B = []

array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort(reverse=True)

k_count = 0
for i in range(n):
    if array_A[i] < array_B[i]:
        array_A[i], array_B[i] = array_B[i], array_A[i]
        k_count += 1
    if k_count == k:
        break


print(sum(array_A))