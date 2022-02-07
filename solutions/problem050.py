from collections import Counter

def solution(clothes):
    category = Counter([x[1] for x in clothes])
    answer = 1
    for count in category.values():
        answer *= count+1
    answer -= 1
    return answer