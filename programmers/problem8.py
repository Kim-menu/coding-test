def adjacent(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]: count += 1
    return count == 1

def solution(begin, target, words):
    BFS = []
    answer = 0
    distance = [0]*len(words)
    BFS.append(-1)
    while BFS:
        cur_idx = BFS.pop(0)
        if cur_idx == -1:
            cur_word = begin
            cur_distance = 0
        else:
            cur_word = words[cur_idx]
            cur_distance = distance[cur_idx]
        if cur_word == target:
            answer = cur_distance
            break
        else:
            for i in range(len(words)):
                if distance[i] == 0 and adjacent(cur_word, words[i]):
                    distance[i] = cur_distance + 1
                    BFS.append(i)
    return answer