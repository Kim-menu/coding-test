def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        prefix = len(phone_book[i])
        if len(phone_book[i+1]) >= prefix:
            if phone_book[i+1][:prefix] == phone_book[i]:
                answer = False
    return answer