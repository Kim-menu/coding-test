import math


def min_tower(start, end, w):
    cover = 2*w + 1
    return math.ceil((end - start + 1) / cover)


def solution(n, stations, w):
    answer = 0
    grey_part = []
    left = 1
    for station in stations:
        right = max(0, station - w - 1)
        if left <= right:
            grey_part.append((left, right))
        left = min(station + w + 1, n + 1)
    right = n
    if left <= right:
        grey_part.append((left, right))
    for (start, end) in grey_part:
        answer += min_tower(start, end, w)
    return answer