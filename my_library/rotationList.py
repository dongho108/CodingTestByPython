
# 반시계방향 90도 회전
def rotation(key):
    newlist = [[0]*len(key) for i in range(len(key[0]))]
    ki = len(key[0])-1
    for i in range(len(newlist)):
        kj = 0
        for j in range(len(newlist[0])):
            newlist[i][j] = key[kj][ki]
            kj += 1
        ki -= 1
    return newlist

key = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotation(key))