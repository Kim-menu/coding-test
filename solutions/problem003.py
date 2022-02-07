def solution(n, results):
    win_matrix = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        win_matrix[i][i] = 1

    for each_edge in results:
        win_matrix[each_edge[1]][each_edge[0]] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                win_matrix[j][k] = min(win_matrix[j][k], win_matrix[j][i] + win_matrix[i][k])

    answer = 0

    for i in range(1, n + 1):
        count = 1
        for j in range(1, n + 1):
            if win_matrix[i][j] + win_matrix[j][i] >= 2 * int(1e9):
                count = 0
                break
        answer += count

    return answer