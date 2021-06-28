def floyd_warshall(n, fares, fw_matrix):
    for [r, c, v] in fares:
        fw_matrix[r - 1][c - 1] = v
        fw_matrix[c - 1][r - 1] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if fw_matrix[i][j] > fw_matrix[i][k] + fw_matrix[k][j]:
                    fw_matrix[i][j] = fw_matrix[i][k] + fw_matrix[k][j]


def solution(n, s, a, b, fares):
    fw_matrix = [[int(1e9)] * n for _ in range(n)]
    for i in range(n):
        fw_matrix[i][i] = 0
    floyd_warshall(n, fares, fw_matrix)
    min_cost = fw_matrix[s - 1][a - 1] + fw_matrix[s - 1][b - 1]
    for i in range(n):
        if fw_matrix[s - 1][i] + fw_matrix[i][a - 1] + fw_matrix[i][b - 1] < min_cost:
            min_cost = fw_matrix[s - 1][i] + fw_matrix[i][a - 1] + fw_matrix[i][b - 1]
    answer = min_cost
    return answer