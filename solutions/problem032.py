def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 0
    recent_camera = -30001
    for i, path in enumerate(routes):
        if path[0] > recent_camera:
            recent_camera = path[1]
            answer += 1
    return answer