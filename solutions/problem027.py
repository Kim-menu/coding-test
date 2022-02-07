def solution(n, k, cmd):
    row = [[i - 1, i, i + 1] for i in range(n)]  # prev, self, next를 저장 (linked_list구현 목적)
    trash = []
    cursor = k
    for cur_cmd in cmd:
        if cur_cmd[0] == 'U':
            count = int(cur_cmd[2:])
            while count:
                cursor = row[cursor][0]
                count -= 1
        elif cur_cmd[0] == 'D':
            count = int(cur_cmd[2:])
            while count:
                cursor = row[cursor][2]
                count -= 1
        elif cur_cmd[0] == 'C':
            trash.append(row[cursor][1])  #
            prev_node = row[cursor][0]
            next_node = row[cursor][2]
            if prev_node > -1:
                row[prev_node][2] = next_node
            if next_node < n:
                row[next_node][0] = prev_node
            if row[cursor][2] == n:  # 삭제된 행이 가장 마지막 행인 경우
                cursor = row[cursor][0]
            else:
                cursor = row[cursor][2]
        else:
            name = trash.pop()
            prev_node = row[name][0]
            next_node = row[name][2]
            if prev_node > -1:
                row[prev_node][2] = name
            if next_node < n:
                row[next_node][0] = name

    answer_list = ['O' for _ in range(n)]
    answer = ''
    for name in trash:
        answer_list[name] = 'X'
    answer = ''.join(answer_list)
    return answer