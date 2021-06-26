def solution(gems):
    gem_set = set(gems)
    total_kind = len(gem_set)
    test_set = set()
    for i in range(len(gems)):
        test_set.add(gems[i])
        if len(test_set) == total_kind:
            end_point = i
            break
    test_set.clear()
    for i in range(end_point, -1, -1):
        test_set.add(gems[i])
        if len(test_set) == total_kind:
            start_point = i
            break
    test_set.clear()
    gem_count = dict()
    for i in range(start_point, end_point + 1):
        if gems[i] in gem_count:
            gem_count[gems[i]] += 1
        else:
            gem_count[gems[i]] = 1
    sol_start, sol_end = start_point + 1, end_point + 1
    distance = end_point - start_point
    if distance > 0 :
        if gem_count[gems[start_point]] == 1:
            gem_set.remove(gems[start_point])
        gem_count[gems[start_point]] -= 1
        start_point += 1
        while end_point < len(gems):
            if len(gem_set) == total_kind:
                sol_start, sol_end = start_point + 1, end_point + 1
                distance = end_point - start_point
                if distance > 0:
                    if gem_count[gems[start_point]] == 1:
                        gem_set.remove(gems[start_point])
                    gem_count[gems[start_point]] -= 1
                    start_point += 1
                    continue
            else:
                if gem_count[gems[start_point]] == 1:
                    gem_set.remove(gems[start_point])
                gem_count[gems[start_point]] -= 1
                start_point += 1
                end_point += 1
                if end_point < len(gems):
                    gem_count[gems[end_point]] += 1
                    gem_set.add(gems[end_point])
    answer = []
    answer.extend([sol_start, sol_end])
    return answer