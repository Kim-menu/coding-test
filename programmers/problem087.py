import heapq
import sys


N = int(input())
min_heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if not min_heap:
            print(0)
        else:
            abs_val, real_val = heapq.heappop(min_heap)
            print(real_val)
    elif x > 0:
        heapq.heappush(min_heap, (x, x))
    else:
        heapq.heappush(min_heap, (-x, x))