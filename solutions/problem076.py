def solution(strs, t):
    dp = [int(1e9)]*(len(t)+1)
    dp[0] = 0
    for i in range(1, len(t)+1):
        last_char = t[i-1]
        for each_piece in strs:
            if each_piece[-1] == last_char and len(each_piece) <= i:
                if t[i-len(each_piece):i] == each_piece:
                    dp[i] = min(dp[i], 1 + dp[i-len(each_piece)])
    answer = dp[len(t)] if dp[len(t)] < int(1e9) else -1
    return answer