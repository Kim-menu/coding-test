def available(dp, i, j):
    ret = []
    if j > 0:
        ret.append(dp[i-1][j-1])
    if j < i:
        ret.append(dp[i-1][j])
    return ret

def solution(triangle):
    height = len(triangle)
    dp = [[0]*(i+1) for i in range(height)]
    dp[0][0] = triangle[0][0]
    for i in range(1, height):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + max(available(dp, i, j))
    answer = max(dp[height-1])
    return answer