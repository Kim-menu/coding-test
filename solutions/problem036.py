def solution(a):
    n = len(a)
    left_min = [a[0]] * n
    right_min = [a[-1]] * n
    for i in range(1, n):
        left_min[i] = a[i] if a[i] < left_min[i-1] else left_min[i-1]
        right_min[n-i-1] = a[n-i-1] if a[n-i-1] < right_min[n-i] else right_min[n-i]
    answer = 0
    for i, element in enumerate(a):
        if i == 0 or i == n-1:
            answer += 1
        else:
            if max(left_min[i-1], element, right_min[i+1]) != element:
                answer += 1
    return answer