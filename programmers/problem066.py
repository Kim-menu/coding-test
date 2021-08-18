def solution(citations):
    citations.sort()
    answer = 0
    for (i, cite) in enumerate(citations):
        h = min(len(citations)-i, cite)
        answer = max(answer, h)
    return answer