N, M = map(int, input().split())
dp = [[int(1e9)]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if i == j: dp[i][j] = 0

for _ in range(M):
    i, j = map(int, input().split())
    dp[i][j] = 1
    dp[j][i] = 1

X, K = map(int, input().split())

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

sol = dp[1][K] + dp[K][X]
if  sol > int(1e9): print(-1)
else: print(sol)