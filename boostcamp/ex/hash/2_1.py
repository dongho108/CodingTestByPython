def solution(phone_book):
    answer = True

    phone_book.sort()
    print(phone_book)

    for i in range(len(phone_book)-1):
        if list(phone_book[i]) == list(phone_book[i+1])[:len(phone_book[i])]:
            return False

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))