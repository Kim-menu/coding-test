def str_to_min(time_str):
    h = int(time_str[0:2])
    m = int(time_str[3:5])
    return h*60 + m


def min_to_str(time_min):
    h = time_min // 60
    m = time_min % 60
    h_str, m_str = map(str, [h, m])
    return h_str.zfill(2)+":"+m_str.zfill(2)


def solution(n, t, m, timetable):
    mintable = []
    for crew in timetable:
        mintable.append(str_to_min(crew))
    mintable.sort()
    bustime = []
    cur_bus = int(9*60)
    for i in range(n):
        bustime.append(cur_bus + i*t)
    for i in range(len(bustime)):
        remain = m
        while len(mintable) > 0 and remain:
            if mintable[0] <= bustime[i]:
                last_crew = mintable.pop(0)
                remain -= 1
            else:
                break
        if i == len(bustime) - 1 :
            if remain:
                answer_int = bustime[i]
            else:
                answer_int = last_crew - 1
    answer = min_to_str(answer_int)
    return answer