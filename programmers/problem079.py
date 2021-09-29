def solution(enter, leave):
    answer = [0]*len(enter)
    cur_room = set()
    leave.reverse()
    enter.reverse()
    while leave:
        cur_left = leave.pop()
        if cur_left not in cur_room:
            cur_enter = -1
            while cur_enter != cur_left:
                cur_enter = enter.pop()
                answer[cur_enter-1] += len(cur_room)
                for entry in cur_room:
                    answer[entry-1] += 1
                cur_room.add(cur_enter)
        cur_room.remove(cur_left)
    return answer