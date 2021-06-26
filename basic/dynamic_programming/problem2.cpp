N, M = map(int, input().split())

money = []
min_money = 10001
dp = [0]*10001

for _ in range(N):
    arg = int(input())
    if arg < min_money: min_money = arg
    dp[arg] = 1
    money.append(arg)

for i in range(min_money):
    dp[i] = 10001

for i in range(min_money, M+1):
    if dp[i] == 0:
        cases = []
        for each_money in money:
            if i-each_money > 0:
                cases.append(dp[i-each_money])
        dp[i] = 1 + min(cases)

if dp[M] > 10000: print(-1)
else: print(dp[M])