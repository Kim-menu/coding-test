from collections import Counter

def solution(participant, completion):
    answer = ''
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    for person, count in c_counter.items():
        p_counter[person] -= count
    for person, count in p_counter.items():
        if count > 0:
            answer = person
            break
    return answer