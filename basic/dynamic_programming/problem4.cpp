N = int(input())
power = list(map(int, input().split()))

dp = [0]*N
dp[0] = 1
soldier_max = 1
for i in range(1, N):
    pre_max = 0
    for j in range(0, i):
        if power[j] > power[i]:
            if pre_max < dp[j]: pre_max = dp[j]
    dp[i] = pre_max + 1
    if soldier_max < dp[i] : soldier_max = dp[i]
print(N-soldier_max)