from collections import deque


def tower_count(edge, start_point, n):
    travel = [0]*(n+1)
    BFS = deque()
    BFS.append(start_point)
    travel[start_point] = 1
    count = 0
    while BFS:
        cur_point = BFS.popleft()
        count += 1
        for adjacent_point in edge[cur_point]:
            if not travel[adjacent_point]:
                BFS.append(adjacent_point)
                travel[adjacent_point] = 1
    return count


def solution(n, wires):
    edge = dict()
    answer = int(1e9)
    for i in range(n+1):
        edge[i] = set()
    for v in wires:
        edge[v[0]].add(v[1])
        edge[v[1]].add(v[0])
    for v in wires:
        edge[v[0]].remove(v[1])
        edge[v[1]].remove(v[0])
        answer = min(answer, abs(tower_count(edge, v[0], n) - tower_count(edge, v[1], n)))
        edge[v[0]].add(v[1])
        edge[v[1]].add(v[0])
    return answer