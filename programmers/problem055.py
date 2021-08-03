from collections import deque


def solution(numbers, target):
    BFS = deque([[numbers[0]], [-numbers[0]]])
    answer = 0
    while BFS:
        cur_seq = BFS.popleft()
        next_idx = len(cur_seq)
        if next_idx < len(numbers):
            BFS.append(cur_seq + [numbers[next_idx]])
            BFS.append(cur_seq + [-numbers[next_idx]])
        else: #다채운 경우
            if sum(cur_seq) == target:
                answer += 1
    return answer