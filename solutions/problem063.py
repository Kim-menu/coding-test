def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        done = 0
        cur = people.pop()
        remain = limit - cur
        while done == 0:
            if people:
                if people[0] <= remain:
                    add_person = people.pop(0)
                    done = 1
                else: #더이상 실을 수 없음
                    done = 1
        answer += 1
    return answer