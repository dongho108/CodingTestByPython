n = list(map(int, input()))

left = 0
right = 0
half = len(n) // 2

for i in range(half):
    left += n[i]
    right += n[i+half]

if left == right:
    print("LUCKY")
else:
    print("READY")
