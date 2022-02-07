def solution(n, works):
    works.sort(reverse=True)
    start = 0
    while n > 0 and works[0] != 0:
        end = len(works)-1
        sub = works[0]
        for i, val in enumerate(works):
            if works[start] > works[i]:
                end = i-1
                sub = works[start] - works[i]
                break
        count = end - start + 1
        if n > sub * count:
            for i in range(start, end + 1):
                works[i] -= sub
            n -= sub * count
            continue
        else:
            quotient = n // count
            remain = n % count
            for i in range(start, end + 1):
                works[i] -= quotient
            for i in range(remain):
                works[start + i] -= 1
            n = 0
    answer = 0
    for val in works:
        answer += val*val
    return answer