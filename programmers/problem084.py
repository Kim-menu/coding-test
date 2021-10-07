from collections import deque

N, M = map(int, input().split())
Edge = dict()
for i in range(N):
    Edge[i+1] = set()
indegree = [0]*N
for _ in range(M):
    A, B = map(int, input().split())
    indegree[B-1] += 1
    Edge[A].add(B)
zero_queue = deque()
for i in range(N):
    if indegree[i] == 0:
        zero_queue.append(i+1)
answer = []
while zero_queue:
    vertex = zero_queue.popleft()
    answer.append(vertex)
    for dest in Edge[vertex]:
        indegree[dest-1] -= 1
        if indegree[dest-1] == 0:
            zero_queue.append(dest)
answer_str = " ".join(map(str, answer))
print(answer_str)