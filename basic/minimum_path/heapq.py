import heapq


def dijkstra():
    global max_time
    global reach_count

    if len(c_q) == 0: return

    (dist_from, node_from) = heapq.heappop(c_q)
    if max_time < dist_from: max_time = dist_from

    if c_traverse[node_from]: pass
    else:
        c_traverse[node_from] = 1
        reach_count += 1
        for edge in road[node_from]:
            c_min_distance[edge[0]] = min(c_min_distance[edge[0]], dist_from + edge[1])
            heapq.heappush(c_q, (c_min_distance[edge[0]], edge[0]))
    dijkstra()

N, M, C = map(int, input().split())

road = [[] for _ in range(N+1)]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    road[X].append((Y, Z))

c_q = []
c_min_distance = [int(1e9)] * (N+1)
c_traverse = [0] * (N+1)
c_min_distance[C] = 0
reach_count = -1;
max_time = 0;
heapq.heappush(c_q, (0, C))
dijkstra()
print(reach_count, max_time)