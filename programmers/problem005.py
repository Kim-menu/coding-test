def transform(h, m, s, ms):
    return ms + s * 1000 + m * 60 * 1000 + h * 60 * 60 * 1000


def include(interval, value):
    if interval[0] <= value <= interval[1]:
        return True
    else:
        return False


def solution(lines):
    reform_lines = []
    for log_data in lines:
        date_s, response_s, duration_s = log_data.split()
        h_s, m_s, sms_s = response_s.split(':')
        s_s, ms_s = sms_s.split('.')
        duration_s = duration_s[:-1]
        duration = int(float(duration_s) * 1000)
        h, m, s, ms = map(int, [h_s, m_s, s_s, ms_s])
        start_time = transform(h, m, s, ms) + 3000 - duration + 1
        end_time = transform(h, m, s, ms) + 3000
        reform_lines.append([start_time, end_time])

    reform_lines.sort()
    answer = 0
    for [start, end] in reform_lines:
        interval = [end, end + 999]
        count = 0
        for [inspect_start, inspect_end] in reform_lines:
            if include(interval, inspect_start) or include(interval, inspect_end):
                count += 1
            elif inspect_start < interval[0] and inspect_end > interval[1]:
                count += 1
        answer = count if answer < count else answer

    return answer