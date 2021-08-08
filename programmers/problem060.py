import heapq


def solution(scoville, K):
    scoville_heap = []
    answer = 0
    for food in scoville:
        heapq.heappush(scoville_heap, food)
    cur1 = heapq.heappop(scoville_heap)
    while cur1 < K:
        if not scoville_heap: #더이상 조합할 음식이 없을 경우 (불가능)
            answer = -1
            break
        cur2 = heapq.heappop(scoville_heap)
        heapq.heappush(scoville_heap, cur1 + cur2*2)
        answer += 1
        cur1 = heapq.heappop(scoville_heap)
    return answer