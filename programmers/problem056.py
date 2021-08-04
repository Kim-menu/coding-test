def need_control(alphabet):
    decision = (ord('Z') - ord('A')) // 2  # 12
    if ord(alphabet) - ord('A') > decision:
        return ord('Z') - ord(alphabet) + 1
    else:
        return ord(alphabet) - ord('A')


def distance(n, a, b):
    start = min(a, b)
    end = max(a, b)
    return min(end - start, start + n - end)


def solution(name):
    answer = 0
    move_list = []
    for i, alphabet in enumerate(name):
        answer += need_control(alphabet)
        if alphabet != 'A':
            move_list.append(i)
    cur_idx = 0
    target = 0
    while move_list:
        min_distance = 100
        for candidate in move_list:
            if min_distance > distance(len(name), cur_idx, candidate):
                target = candidate
                min_distance = distance(len(name), cur_idx, candidate)
        answer += min_distance
        move_list.remove(target)
        cur_idx = target
    return answer