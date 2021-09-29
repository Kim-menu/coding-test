import copy


def not_operate(board):
    not_board = [[0] * len(board) for _ in range(len(board))]
    for row in range(len(board)):
        for col in range(len(board)):
            not_board[row][col] = 0 if board[row][col] else 1
    return not_board


def adjacent_list(row, col, n):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    adj = []
    for i in range(4):
        if 0 <= row+dr[i] < n and 0 <= col+dc[i] < n:
            adj.append((row+dr[i], col+dc[i]))
    return adj


def get_segment_list(board):
    segment_list = []
    test_board = copy.deepcopy(board)
    for row in range(len(test_board)):
        for col in range(len(test_board)):
            if test_board[row][col] == 1:
                cur_segment = [[0] * len(test_board) for _ in range(len(test_board))]
                DFS = [(row, col)]
                test_board[row][col] = 0
                cur_segment[row][col] = 1
                while DFS:
                    cur_row, cur_col = DFS.pop()
                    for adj_row, adj_col in adjacent_list(cur_row, cur_col, len(test_board)):
                        if test_board[adj_row][adj_col] == 1:
                            test_board[adj_row][adj_col] = 0
                            cur_segment[adj_row][adj_col] = 1
                            DFS.append((adj_row, adj_col))
                segment_list.append(cur_segment)
    return segment_list


def get_rotate_list(segment):
    rotate_list = [segment]
    for i in range(3):
        rotate = [[0] * len(segment) for _ in range(len(segment))]
        for row in range(len(segment)):
            for col in range(len(segment)):
                rotate[col][len(segment)-1-row] = rotate_list[i][row][col]
        rotate_list.append(rotate)
    return rotate_list


def move_seg(segment, dr, dc):
    after_segment = [[0] * len(segment) for _ in range(len(segment))]
    for row in range(len(segment)):
        for col in range(len(segment)):
            if segment[row][col] == 1:
                if 0 <= row+dr < len(segment) and 0 <= col+dc < len(segment):
                    after_segment[row+dr][col+dc] = 1
                else:
                    after_segment[0][0] = -1
                    return after_segment
    return after_segment


def match(seg1, seg2):
    seg1_first_pos = [-1, -1]
    seg2_first_pos = [-1, -1]
    for row in range(len(seg1)):
        for col in range(len(seg2)):
            if seg1_first_pos[0] != -1 and seg2_first_pos[0] != -1:
                break
            if seg1[row][col] == 1 and seg1_first_pos[0] == -1:
                seg1_first_pos[0] = row
                seg1_first_pos[1] = col
            if seg2[row][col] == 1 and seg2_first_pos[0] == -1:
                seg2_first_pos[0] = row
                seg2_first_pos[1] = col
    seg2 = move_seg(seg2, seg1_first_pos[0] - seg2_first_pos[0], seg1_first_pos[1] - seg2_first_pos[1])
    return seg1 == seg2


def exist_match(fix_seg, mov_seg):
    mov_seg_list = get_rotate_list(mov_seg)
    for cur_seg in mov_seg_list:
        if match(fix_seg, cur_seg):
            return True
    return False


def size_compare(seg1, seg2):
    seg1_sum = sum([sum(row) for row in seg1])
    seg2_sum = sum([sum(row) for row in seg2])
    return seg1_sum == seg2_sum


def solution(game_board, table):
    answer = 0
    fix_seg_list = get_segment_list(not_operate(game_board))
    mov_seg_list = get_segment_list(table)
    for cur_blank in fix_seg_list:
        for i in range(len(mov_seg_list)):
            if not size_compare(cur_blank, mov_seg_list[i]):
                continue
            if exist_match(cur_blank, mov_seg_list[i]):
                answer += sum([sum(row) for row in mov_seg_list[i]])
                del mov_seg_list[i]
                break
    return answer