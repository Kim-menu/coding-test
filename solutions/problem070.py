from collections import Counter


def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    scores_inverse = [[0] * len(scores) for _ in range(len(scores))]
    for i in range(len(scores)):
        for j in range(len(scores)):
            scores_inverse[j][i] = scores[i][j]
    answer = ''
    for row in range(len(scores_inverse)):
        post_sub, div_num = 0, len(scores_inverse[row])
        score_counter = Counter(scores_inverse[row])
        if scores_inverse[row][row] == min(scores_inverse[row]) or scores_inverse[row][row] == max(scores_inverse[row]):
            if score_counter[scores_inverse[row][row]] == 1:
                post_sub, div_num = scores_inverse[row][row], len(scores_inverse[row]) - 1
        average = (sum(scores_inverse[row]) - post_sub) / div_num
        answer += grade(average)
    return answer