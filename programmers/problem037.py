from collections import Counter


def solution(a):
    if len(a) < 2:
        return 0
    answer = 2
    elem_counter = Counter(a)
    count_list = [(k, v) for (k, v) in elem_counter.items()]
    count_list.sort(reverse=True, key=lambda x: x[1])
    for (elem, count) in count_list:
        if count <= answer // 2: break
        left = 0
        right = 1
        summation = 0
        while right < len(a):
            if a[left] == elem:
                if a[right] != elem:
                    summation += 2
                    left = right + 1
                    right = left + 1
                else:
                    right += 1
            elif a[right] == elem:
                summation += 2
                left = right + 1
                right = left + 1
            else:
                left = right
                right = left + 1
        answer = max(summation, answer)
    return answer
