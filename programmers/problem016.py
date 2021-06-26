import heapq

def solution(operations):
    max_q = []
    min_q = []
    for cur_oper in operations:
        if cur_oper[0] == 'I':
            number = int(cur_oper[2:])
            heapq.heappush(min_q, number)
            heapq.heappush(max_q, -number)
        elif cur_oper == "D 1":
            if len(max_q) > 0:
                number = heapq.heappop(max_q)
                min_q.remove(-number)
        else:
            if len(max_q) > 0:
                number = heapq.heappop(min_q)
                max_q.remove(-number)
    answer = []
    if len(max_q) == 0:
        answer = [0, 0]
    else:
        answer.append(-heapq.heappop(max_q))
        answer.append(heapq.heappop(min_q))
    return answer