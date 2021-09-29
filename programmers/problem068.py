def solution(money):
    case = ["first_include", "last_include"]
    money_list = []
    for each_case in case:
        start = 0 if each_case == "first_include" else 1
        end = len(money)-2 if each_case == "first_include" else len(money)-1
        dp = [0]*len(money)
        for i in range(start, end+1):
            candidate = [money[i]]
            if i-2 >= 0:
                candidate.append(money[i]+dp[i-2])
            if i-3 >= 0:
                candidate.append(money[i]+dp[i-3])
            dp[i] = max(candidate)
        money_list += [dp[end], dp[end-1]]
    answer = max(money_list)
    return answer