def bit_idx(arg):
    if arg == 0: return 0b01 #기둥
    else: return 0b10 #보

def condition(x, y, struct_type, cmd_type, structure):
    result = 1
    if struct_type == 0: #기둥
        if cmd_type == 0: #삭제
            structure[x][y] &= bit_idx(not 0)
            if structure[x][y+1] & bit_idx(0):
                result &= condition(x, y+1, 0, 1, structure)
            if x > 0 and structure[x-1][y+1] & bit_idx(1):
                result &= condition(x-1, y+1, 1, 1, structure)
            if structure[x][y+1] & bit_idx(1):
                result &= condition(x, y+1, 1, 1, structure)
            structure[x][y] |= bit_idx(0)
        else: #설치
            result = 0
            if y == 0: result = 1
            elif x > 0 and structure[x-1][y] & bit_idx(1): result = 1
            elif structure[x][y] & bit_idx(1): result = 1
            elif structure[x][y-1] & bit_idx(0): result = 1
    else:   #보
        if cmd_type == 0: #삭제
            structure[x][y] &= bit_idx(not 1)
            if structure[x][y] & bit_idx(0):
                result &= condition(x, y, 0, 1, structure)
            if structure[x+1][y] & bit_idx(0):
                result &= condition(x+1, y, 0, 1, structure)
            if x > 0 and structure[x-1][y] & bit_idx(1):
                result &= condition(x-1, y, 1, 1, structure)
            if x < len(structure) - 1 and structure[x+1][y] & bit_idx(1):
                result &= condition(x+1, y, 1, 1, structure)
            structure[x][y] |= bit_idx(1)
        else: #설치
            result = 0
            if y > 0 and structure[x][y-1] & bit_idx(0): result = 1
            elif y > 0 and structure[x+1][y-1] & bit_idx(0): result = 1
            elif 0 < x < len(structure) - 1 and structure[x-1][y] & structure[x+1][y] & bit_idx(1): result = 1
    return result


def solution(n, build_frame):
    structure = [[0]*(n+1) for _ in range(n+1)]
    for [x, y, struct_type, cmd_type] in build_frame:
        if condition(x, y, struct_type, cmd_type, structure):
            if cmd_type == 0:
                structure[x][y] &= bit_idx(not struct_type)
            else:
                structure[x][y] |= bit_idx(struct_type)
    answer = []
    for i in range(len(structure)):
        for j in range(len(structure)):
            if structure[i][j] & bit_idx(0):
                answer.append([i, j, 0])
            if structure[i][j] & bit_idx(1):
                answer.append([i, j, 1])
    return answer