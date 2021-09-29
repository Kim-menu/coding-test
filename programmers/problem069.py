def solution(price, money, count):
    initial = count + 1
    while count:
        money -= price*(initial - count)
        count -= 1
    answer = max(-money, 0)
    return answer