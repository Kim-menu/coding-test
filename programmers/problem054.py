from collections import deque

def solution(progresses, speeds):
    pro_q = deque(progresses)
    spd_q = deque(speeds)
    answer = []
    while len(pro_q) > 0:
        for i in range(len(pro_q)):
            pro_q[i] += spd_q[i]
        count = 0
        while pro_q:
            if pro_q[0] >= 100:
                pro_q.popleft()
                spd_q.popleft()
                count += 1
            else:
                break
        if count:
            answer.append(count)
    return answer