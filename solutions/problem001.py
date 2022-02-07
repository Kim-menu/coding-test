def n_digit(N, digit):
    result = 0
    for i in range(digit):
        result += N*pow(10, i)
    return result

def cross_join(A, B):
    result = []
    for a in A:
        for b in B:
            result.append(a+b)
            if a-b > 0: result.append(a-b)
            result.append(a*b)
            if a//b > 0: result.append(a//b)
    return result

def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(n_digit(N, i))
        for j in range(1, i):
            dp[i].update(cross_join(dp[j], dp[i-j]))
        if number in dp[i]:
            answer = i
            break
    return answer