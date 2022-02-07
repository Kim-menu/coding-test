from collections import deque

def solution(answers):
    people = []
    people.append(deque([1, 2, 3, 4, 5]))
    people.append(deque([2, 1, 2, 3, 2, 4, 2, 5]))
    people.append(deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]))
    count = [0, 0, 0]
    for num in answers:
        people_sol = []
        for i in people:
            people_sol.append(i.popleft())
        for i, val in enumerate(people_sol):
            if val == num:
                count[i] += 1
            people[i].append(val)
    answer = [i+1 for i in range(len(count)) if count[i] == max(count)]
    return answer