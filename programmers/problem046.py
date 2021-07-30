def hanoi(src, dst, n):
    remain = list({1, 2, 3} - {src, dst})
    temp = remain[0]
    if n == 1:
        return [[src, dst]]
    else:
        return hanoi(src, temp, n-1) + hanoi(src, dst, 1) + hanoi(temp, dst, n-1)

def solution(n):
    answer = hanoi(1, 3, n)
    return answer