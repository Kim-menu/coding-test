def valid(stones, k, n):
    zero_count = 0
    for stone in stones:
        if stone - n <= 0:
            zero_count += 1
        else:
            zero_count = 0
        if zero_count >= k:
            return False
    return True


def solution(stones, k):
    left = min(stones) - 1
    right = max(stones)

    while left < right - 1:
        middle = (left + right) // 2
        if valid(stones, k, middle):
            left = middle
        else:
            right = middle
    answer = right
    return answer
