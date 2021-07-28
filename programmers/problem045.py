def solution(n, s):
    if s < n:
        return [-1]
    quotient = s // n
    remain = s % n
    answer = [quotient for _ in range(n)]
    for i in range(n-1, n-1-remain, -1):
        answer[i] += 1
    return answer
