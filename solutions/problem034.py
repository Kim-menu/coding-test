from collections import deque

def move_result(board, position):
    result = []
    n = len(board)
    (x1, y1) = position[0]
    (x2, y2) = position[1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4): #동서남북
        if board[x1+dx[i]][y1+dy[i]] == 0 and board[x2+dx[i]][y2+dy[i]] == 0:
            result.append(((x1+dx[i], y1+dy[i]), (x2+dx[i], y2+dy[i])))
    #회전
    if x1 == x2: #가로
        for direction in [-1, 1]: #up, down
            if board[x1+direction][y1] == 0 and board[x1+direction][y2] == 0:
                result.append(((x1+direction, y1), (x1, y1)))
                result.append(((x1+direction, y2), (x1, y2)))
    else: #세로
        for direction in [-1, 1]: #left, right
            if board[x1][y1+direction] == 0 and board[x2][y1+direction] == 0:
                result.append(((x1, y1+direction), (x1, y1)))
                result.append(((x2, y1+direction), (x2, y1)))
    return result



def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(1, len(new_board)-1):
        for j in range(1, len(new_board)-1):
            new_board[i][j] = board[i-1][j-1]
    answer = -1
    queue = deque()
    traverse = set()
    queue.append(((1,1), (1,2), 0))
    while queue:
        cur1, cur2, cur_count = queue.popleft()
        if (n, n) in [cur1, cur2]:
            answer = cur_count
            break
        for next_pos in move_result(new_board, (cur1, cur2)):
            if next_pos not in traverse: #방문한 적 없는 경우
                traverse.add((next_pos[0], next_pos[1]))
                queue.append((next_pos[0], next_pos[1], cur_count + 1))
    return answer