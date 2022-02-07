def hms_to_sec(hms_str):
    H, M, S = hms_str[0:2], hms_str[3:5], hms_str[6:8]
    sec = int(S)
    sec += int(M) * 60
    sec += int(H) * 3600
    return sec


def sec_to_hms(sec):
    H = sec // 3600
    sec = sec % 3600
    M = sec // 60
    sec = sec % 60
    S = sec
    hms_str = str(H).zfill(2) + ":" + str(M).zfill(2) + ":" + str(S).zfill(2)
    return hms_str


def solution(play_time, adv_time, logs):
    total_time = hms_to_sec(play_time)
    user_add = [0] * (total_time)  # user_add[n] = 1이면 n sec에 start하는 user가 1명 있다는 것
    user_sub = [0] * (total_time + 1)  # user_sub[n] = 1이면 n sec에 end하는 user가 1명 있다는 것
    pre_sum = [0] * (total_time + 1)  # pre_sum[n] = 1이면 0 ~ n 구간에 누적 재생시간이 1이라는 것
    for log in logs:
        start_hms = log[0:8]
        end_hms = log[9:17]
        start_sec = hms_to_sec(start_hms)
        end_sec = hms_to_sec(end_hms)
        user_add[start_sec] += 1
        user_sub[end_sec] += 1
    cur_users = 0
    pre_sum[0] = 0
    adv_sec = hms_to_sec(adv_time)
    adv_max = 0
    adv_start = 0
    for i in range(1, total_time + 1):
        cur_users += user_add[i - 1]
        cur_users -= user_sub[i - 1]
        pre_sum[i] = pre_sum[i - 1] + cur_users
        if i >= adv_sec:
            if adv_max < pre_sum[i] - pre_sum[i - adv_sec]:
                adv_max = pre_sum[i] - pre_sum[i - adv_sec]
                adv_start = i - adv_sec
    answer = sec_to_hms(adv_start)
    return answer