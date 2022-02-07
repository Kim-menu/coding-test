from copy import deepcopy


def valid(row, col, M):
    return 0 <= row < M and 0 <= col < M


def rotate(srce, dest):
    M = len(srce)
    for i in range(M):
        for j in range(M):
            dest[j][M - i - 1] = srce[i][j]


def move(srce, dest, dx, dy):
    M = len(srce)
    for i in range(M):
        for j in range(M):
            if valid(i - dy, j - dx, M):
                dest[i][j] = srce[i - dy][j - dx]
            else:
                dest[i][j] = 0


def find_point(lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0: return j, i
    return -1, -1


def expand(srce, dest):
    for i in range(len(srce)):
        for j in range(len(srce)):
            dest[i][j] = srce[i][j]


def fit(key, lock):
    N = len(key)
    multiply = 1
    for i in range(N):
        for j in range(N):
            multiply *= key[i][j] + lock[i][j]
    return multiply == 1


def solution(key, lock):
    x, y = find_point(lock)
    if (x, y) == (-1, -1): return True
    answer = False
    M = len(key)
    N = len(lock)
    expand_key = [[0] * N for _ in range(N)]
    expand(key, expand_key)

    rotate_set = []
    for _ in range(4):
        rotate_set.append(deepcopy(expand_key))
    for i in range(3):
        rotate(rotate_set[i], rotate_set[i + 1])
    for i in range(4):
        cur_key = deepcopy(rotate_set[i])
        for cur_y in range(N):
            for cur_x in range(N):
                if cur_key[cur_y][cur_x] == 1:
                    dy = y - cur_y
                    dx = x - cur_x
                    test_key = deepcopy(cur_key)
                    move(cur_key, test_key, dx, dy)
                    if fit(test_key, lock): answer = True
    return answer