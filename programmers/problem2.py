def pass_people(time, judges):
    judge_pass = [time // each_judge for each_judge in judges]
    return sum(judge_pass)

def solution(n, times):
    left, right = 1, max(times)*n
    while left != right:
        middle = ( left + right ) // 2
        if pass_people(middle, times) < n:
            left = middle + 1
            continue
        else:
            right = middle
            continue
    answer = left
    return answer