from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)
    cur_weight = 0
    answer = 0
    while truck_queue:
        answer += 1
        cur_weight -= bridge.popleft()
        if cur_weight + truck_queue[0] <= weight:
            next_truck = truck_queue.popleft()
            bridge.append(next_truck)
            cur_weight += next_truck
        else:
            bridge.append(0)
    answer += bridge_length
    return answer