from collections import deque

def available(maze, N, M, row, col, travel, distance):
    result = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= row + dr[i] < N and 0 <= col + dc[i] < M:
            if not travel[row+dr[i]][col+dc[i]] and maze[row+dr[i]][col+dc[i]]:
                travel[row+dr[i]][col+dc[i]] = 1
                result.append((row+dr[i], col+dc[i], distance+1))
    return result


N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

travel = [[0]*M for _ in range(N)]

BFS = deque([(0, 0, 1)])
travel[0][0] = 1

while BFS:
    cur_row, cur_col, cur_distance = BFS.popleft()
    if cur_row == N-1 and cur_col == M-1:
        print(cur_distance)
        break
    BFS.extend(available(maze, N, M, cur_row, cur_col, travel, cur_distance))
