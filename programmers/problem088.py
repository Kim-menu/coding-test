N = int(input())

dp = [int(1e9)]*(N+1)
trace = [-1]*(N+1)

dp[0], dp[1] = 0, 0
for i in range(1, N+1):
    if i+1 <= N and dp[i]+1 < dp[i+1]:
        dp[i+1] = dp[i]+1
        trace[i+1] = i
    if i*2 <= N and dp[i]+1 < dp[i*2]:
        dp[i*2] = dp[i]+1
        trace[i*2] = i
    if i*3 <= N and dp[i]+1 < dp[i*3]:
        dp[i*3] = dp[i]+1
        trace[i*3] = i
print(dp[N])
cur_int = N
back_track = []
while cur_int != -1:
    back_track.append(cur_int)
    cur_int = trace[cur_int]
print(" ".join(map(str, back_track)))