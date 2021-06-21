def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]):
                # print(list(phone_book[i]), list(phone_book[j])[:len(phone_book[i])])
                if list(phone_book[i]) == list(phone_book[j])[:len(phone_book[i])]:
                    return False

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(	["123", "456", "789"]))
print(solution(["12","123","1235","567","88"]))