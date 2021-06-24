def bomb_bag(bag):
    if len(bag) == 0:
        return bag

    print("in bomb bag : ", bag)
    rel = [bag[0]]
    check = False
    for i in range(1, len(bag)):
        if rel[len(rel)-1] == bag[i]:
            check = True
            continue
        else:
            if check:
                rel.pop(-1)
                check = False
            rel.append(bag[i])
            print("rel : ", rel)
    if check:
        rel.pop(-1)

    if rel == bag:
        return rel
    else:
        return (bomb_bag(rel))


def solution(board, moves):
    answer = 0

    bag = []
    pointer = [0 for _ in range(len(board[0]))]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and pointer[j] == 0:
                pointer[j] = i

    for i in range(len(moves)):
        print("==")
        if pointer[moves[i] - 1] != len(board) - 1:
            # print(pointer[moves[i] - 1], i - 1)
            bag.append(board[pointer[moves[i] - 1]][moves[i] - 1])
            bag = bomb_bag(bag)
            print("bag : ", bag)
            board[pointer[moves[i] - 1]][moves[i] - 1] = 0
            pointer[moves[i] - 1] += 1

    return len(bag)

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))