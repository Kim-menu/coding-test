def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    a, b = 0, 0
    answer = 0
    while a < len(A):
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            a += 1
    return answer
