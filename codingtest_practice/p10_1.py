def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()


def rotation_key(tkey, ks):
    rkey = [[0]*ks for _ in range(ks)]

    for i in range(ks):
        for j in range(ks):
            rkey[j][ks-i-1] = tkey[i][j]

    return rkey



def check_key(extendLock):
    lock_length = len(extendLock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if extendLock[i][j] != 1:
                return False
    return True



def solution(key, lock):
    answer = True

    lock_size = len(lock)
    key_size = len(key)

    extendLock = [[0]*lock_size*3 for _ in range(lock_size*3)]

    for i in range(lock_size):
        for j in range(lock_size):
            extendLock[lock_size+i][lock_size+j] += lock[i][j]


    for r in range(4):
        key = rotation_key(key, key_size)

        for a in range(lock_size*2):
            for b in range(lock_size*2):
                for i in range(key_size):
                    for j in range(key_size):
                        extendLock[i+a][j+b] += key[i][j]
                if check_key(extendLock):
                    return True
                for i in range(key_size):
                    for j in range(key_size):
                        extendLock[i + a][j + b] -= key[i][j]
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))