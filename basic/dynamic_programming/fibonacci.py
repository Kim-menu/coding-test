N = int(input())
food = tuple(map(int, input().split()))

dp = [0]*100

dp[0] = food[0]
dp[1] = food[1]
dp[2] = dp[0] + food[2]
for i in range(3, N):
    dp[i] = max(dp[i-2], dp[i-3]) + food[i]

print(max(dp[N-1], dp[N-2]))