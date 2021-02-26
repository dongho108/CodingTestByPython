def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()


def is_match(tlock, ks, ls):
    for i in range(ls):
        for j in range(ls):
            if tlock[i+ks-1][j+ks-1] != 1:
                return False
    return True


def rotation_key(tkey, ks):
    rkey = [[0]*ks for _ in range(ks)]

    for i in range(ks):
        for j in range(ks):
            rkey[i][j] = tkey[ks-1-j][i]

    return rkey


def solution(key, lock):
    answer = True

    lock_size = len(lock)
    key_size = len(key)
    exlock_size = lock_size + 2*(key_size-1)

    expend_lock = [[0]*exlock_size for _ in range(exlock_size)]

    for i in range(lock_size):
        for j in range(lock_size):
            expend_lock[i+key_size-1][j+key_size-1] = lock[i][j]

    for i in range(key_size+lock_size-1):
        for j in range(key_size+lock_size-1):
            for k in range(4):
                rkey = rotation_key(key, key_size)

                for a in range(key_size):
                    for b in range(key_size):
                        expend_lock[i+a][j+b] = expend_lock[i+a][j+b] + rkey[a][b]

                if is_match(expend_lock, key_size, lock_size):
                    return True
                else:
                    for a in range(key_size):
                        for b in range(key_size):
                            expend_lock[i + a][j + b] = expend_lock[i + a][j + b] - rkey[a][b]

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))