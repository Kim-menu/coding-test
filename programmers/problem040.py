def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    result = []
    for case in [0, 1]: #0: 첫번째 원소 포함 #1: 마지막 원소 포함
        start = case
        end = len(sticker) - 2 + case
        dp = [0] * len(sticker)
        dp[case] = sticker[case]
        for i in range(start, end + 1):
            prev_2step = dp[i-2] if i-2 >= start else 0
            prev_3step = dp[i-3] if i-3 >= start else 0
            dp[i] = sticker[i] + max(prev_2step, prev_3step)
        if start < end:
            result.append(max(dp[end], dp[end-1]))
        else:
            result.append(dp[end])
    answer = max(result)
    return answer