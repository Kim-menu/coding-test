def min_remove(each_dist, min_dist):
    cnt = 0
    consider_remove = 0
    for i in range(len(each_dist)):
        if consider_remove + each_dist[i] < min_dist:
            cnt += 1
            consider_remove += each_dist[i]
        else:
            consider_remove = 0
    return cnt


def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    each_dist = []
    for i in range(len(rocks)+1):
        if i == 0:
            each_dist.append(rocks[i] - 0)
        elif i == len(rocks):
            each_dist.append(distance - rocks[i-1])
        else:
            each_dist.append(rocks[i] - rocks[i-1])
    while left < right:
        mid = (left + right) // 2
        if min_remove(each_dist, mid) > n:
            right = mid
        else:
            left = mid + 1
    answer = left-1
    return answer