from collections import deque

queue = deque()

queue.append(3)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순
queue.reverse()
print(queue) #나중에 들어온 순