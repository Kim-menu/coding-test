import heapq

def solution(jobs):
    jobs.sort()
    wait_jobs = []
    complete_jobs = []
    cur_ms = jobs[0][0]
    end_ms = 0
    cur_pointer = 0
    while len(complete_jobs) < len(jobs):
        while cur_pointer < len(jobs):
            if jobs[cur_pointer][0] == cur_ms:
                heapq.heappush(wait_jobs, (jobs[cur_pointer][1], cur_pointer))
                cur_pointer += 1
            elif jobs[cur_pointer][0] > cur_ms:
                break
        if cur_ms >= end_ms and wait_jobs:
            duration, index = heapq.heappop(wait_jobs)
            end_ms = cur_ms + duration
            complete_jobs.append((index, jobs[index][0], end_ms))
        cur_ms += 1
    throughput = [each[2] - each[1] for each in complete_jobs]
    answer = sum(throughput) // len(jobs)
    return answer