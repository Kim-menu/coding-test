def solution(n):
    dp = [1] + [0] * (n)
    for i in range(1, n+1):
        for step in [1, 2]:
            if i-step >= 0:
                dp[i] += dp[i-step]
                dp[i] %= 1234567
    answer = dp[n]
    return answer