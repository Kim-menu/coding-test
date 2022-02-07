def solution(n, lost, reserve):
    answer = n
    cloth = [1]*n
    for child in lost:
        cloth[child-1] -= 1
    for child in reserve:
        cloth[child-1] += 1
    for i in range(n):
        if cloth[i] == 0:
            if i > 0 and cloth[i-1] > 1:
                cloth[i] += 1
                cloth[i-1] -= 1
            elif i < n-1 and cloth[i+1] > 1:
                cloth[i] += 1
                cloth[i+1] -= 1
        if cloth[i] == 0:
            answer -= 1
    return answer