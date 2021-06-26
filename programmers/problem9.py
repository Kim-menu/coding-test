def range_in(m, n, x, y):
    return 1 <= x <= m and 1 <= y <= n


def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for [x, y] in puddles:
        dp[y][x] = -1
    for height in range(3, m + n + 1):
        for i in range(1, height):
            x, y = height - i, i
            if range_in(m, n, x, y):
                if dp[y][x] == -1:
                    dp[y][x] = 0
                else:
                    if range_in(m, n, x - 1, y): dp[y][x] += dp[y][x - 1]
                    if range_in(m, n, x, y - 1): dp[y][x] += dp[y - 1][x]
    answer = dp[n][m] % 1000000007
    return answer