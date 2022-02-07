from itertools import permutations


def translate(n, circle, start_point):
    result = []
    for item in circle:
        if item >= start_point:
            result.append(item)
        else:
            result.append(item+n)
    result.sort()
    return result


def simulation(weak, friend):
    result = []
    for each_point in weak:
        if each_point > weak[0] + friend:
            result.append(each_point)
    return result


def solution(n, weak, dist):
    dist.sort(reverse=True)
    answer = int(1e9)
    for start_point in weak:
        for each_case in permutations(dist, len(dist)):
            test_weak = translate(n, weak, start_point)
            cur_case = list(each_case)
            for i, cur_friend in enumerate(cur_case):
                if answer < i+1:
                    break
                test_weak = simulation(test_weak, cur_friend)
                if len(test_weak) == 0:
                    if answer > i+1:
                        answer = i+1
                    break
    if answer == int(1e9):
        answer = -1
    return answer