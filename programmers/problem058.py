def solution(priorities, location):
    priorities_idx = [(priorities[i], i) for i in range(len(priorities))]
    answer = 1
    while len(priorities_idx) > 0:
        (p, i) = priorities_idx[0]
        if p < max(priorities_idx, key = lambda x: x[0])[0]:
            priorities_idx.pop(0)
            priorities_idx.append((p, i))
        else:
            priorities_idx.pop(0)
            if i == location:
                break
            else:
                answer += 1
    return answer