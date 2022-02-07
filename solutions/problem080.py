def max_value(g, s, w, t, T):
    g_result, s_result, total_result = 0, 0, 0
    for i in range(len(t)):
        move = (T // t[i] + 1) // 2
        g_result += min(g[i], w[i] * move)
        s_result += min(s[i], w[i] * move)
        total_result += min(g[i] + s[i], w[i] * move)
    return g_result, s_result, total_result


def solution(a, b, g, s, w, t):
    (left, right) = (0, int(1e15))
    while right > left:
        middle = (left + right) // 2
        g_result, s_result, total_result = max_value(g, s, w, t, middle)
        if g_result >= a and s_result >= b and total_result >= a + b:
            right = middle
        else:
            left = middle + 1
    answer = left
    return answer