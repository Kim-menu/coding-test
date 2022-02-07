# d -> don't care
# u -> up & down
# l -> left & right
def in_range(row, col, board):
    N = len(board)
    return 0 <= row < N and 0 <= col < N and board[row][col] == 0


def BFS(board):
    BFS_queue = []
    N = len(board)
    cost_x = [[int(1e9)]*N for _ in range(N)]
    cost_x[0][0] = 0
    cost_y = [[int(1e9)]*N for _ in range(N)]
    cost_y[0][0] = 0
    cost = dict()
    cost['l'] = cost_x
    cost['u'] = cost_y
    cost['d'] = cost_x
    BFS_queue.append((0, 0, 'd'))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dd = ['l', 'u', 'l', 'u']
    while BFS_queue:
        row, col, direction = BFS_queue.pop(0)
        for i in range(len(dr)):
            (next_row, next_col) = (row + dr[i], col + dc[i])
            add_cost = 100 if dd[i] == direction or direction == 'd' else 600
            next_cost = cost[direction][row][col] + add_cost
            if in_range(next_row, next_col, board) and next_cost <= cost[dd[i]][next_row][next_col]:
                cost[dd[i]][next_row][next_col] = next_cost
                if (next_row, next_col, dd[i]) in BFS_queue:
                    BFS_queue.remove((next_row, next_col, dd[i]))
                BFS_queue.append((next_row, next_col, dd[i]))
    return min(cost['l'][N-1][N-1], cost['u'][N-1][N-1])


def solution(board):
    answer = BFS(board)
    return answer