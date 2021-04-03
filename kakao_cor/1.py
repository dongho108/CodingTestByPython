def solution(gift_cards, wants):
    answer = 0

    for card in gift_cards:
        if card in wants:
            wants.pop(wants.index(card))

    answer = len(wants)


    return answer

print(solution([4, 5, 3, 2, 1], [2, 4, 4, 5, 1]	))
print(solution([5, 4, 5, 4, 5], [1, 2, 3, 5, 4]	))
