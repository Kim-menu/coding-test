def solution(number, k):
    answer = ''
    must_choose = len(number) - k
    last_choose = -1
    while must_choose:
        cur_max, max_idx = '\0', -1
        for i in range(last_choose + 1, len(number) - must_choose + 1):
            if number[i] > cur_max:
                cur_max = number[i]
                max_idx = i
                if number[i] == '9':
                    break
        last_choose = max_idx
        answer += cur_max
        must_choose -= 1
    return answer