import copy


def delta(board, r, c, cmd):
    dr = r
    dc = c
    if cmd == "u":
        if dr > 0: dr -= 1
    elif cmd == "d":
        if dr < len(board) - 1: dr += 1
    elif cmd == "r":
        if dc < len(board) - 1: dc += 1
    elif cmd == "l":
        if c > 0: dc -= 1
    elif cmd == "cu":
        while dr > 0:
            dr -= 1
            if board[dr][dc] > 0:
                break
    elif cmd == "cd":
        while dr < len(board) - 1:
            dr += 1
            if board[dr][dc] > 0:
                break
    elif cmd == "cr":
        while dc < len(board) - 1:
            dc += 1
            if board[dr][dc] > 0:
                break
    else:
        while dc > 0:
            dc -= 1
            if board[dr][dc] > 0:
                break
    return dr, dc


def smallest_click(board, r1, c1, r2, c2):
    n = len(board)
    cmd = ["u", "d", "r", "l", "cu", "cd", "cr", "cl"]
    queue = [(r1, c1, 1)]
    traverse = [[0] * n for _ in range(n)]
    traverse[r1][c1] = 1
    while queue:
        (cur_r, cur_c, cur_click) = queue.pop(0)
        if (cur_r, cur_c) == (r2, c2):
            return cur_click
        for each_cmd in cmd:
            next_r, next_c = delta(board, cur_r, cur_c, each_cmd)
            if not traverse[next_r][next_c]:
                traverse[next_r][next_c] = 1
                queue.append((next_r, next_c, cur_click + 1))
    return -1


def solution(board, r, c):
    total_card = set()
    for i in range(len(board)):
        for j in range(len(board)):
            total_card.add(board[i][j])
    total_card.remove(0)
    pair_list = []
    for each_card in total_card:
        pair = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == each_card:
                    pair.append([i, j])
        pair_list.append(pair)
    case_queue = []
    total_case = []
    for i in range(len(pair_list)):
        case_queue.append([i])
    while case_queue:
        cur_case = case_queue.pop(0)
        if len(cur_case) == len(pair_list):
            total_case.append(cur_case)
            continue
        for i in range(len(pair_list)):
            if i not in cur_case:
                case_queue.append(cur_case + [i])
    min_click = int(1e9)
    for each_case in total_case:
        cur_r = r
        cur_c = c
        click = 0
        test_board = copy.deepcopy(board)
        while each_case:
            target_card = each_case.pop(0)
            first_point = pair_list[target_card][0]
            second_point = pair_list[target_card][1]
            if smallest_click(test_board, cur_r, cur_c, first_point[0], first_point[1]) < smallest_click(test_board, cur_r, cur_c, second_point[0], second_point[1]):
                click += smallest_click(test_board, cur_r, cur_c, first_point[0], first_point[1])
                click += smallest_click(test_board, first_point[0], first_point[1], second_point[0], second_point[1])
                cur_r, cur_c = second_point[0], second_point[1]
            else:
                click += smallest_click(test_board, cur_r, cur_c, second_point[0], second_point[1])
                click += smallest_click(test_board, second_point[0], second_point[1], first_point[0], first_point[1])
                cur_r, cur_c = first_point[0], first_point[1]
            test_board[first_point[0]][first_point[1]] = 0
            test_board[second_point[0]][second_point[1]] = 0
            if click > min_click: break
        if min_click > click: min_click = click
    answer = min_click
    return answer