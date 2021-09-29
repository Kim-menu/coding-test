def solution(sizes):
    max_list = []
    min_list = []
    for card in sizes:
        max_list.append(max(card))
        min_list.append(min(card))
    answer = max(max_list)*max(min_list)
    return answer