def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


def solution(n, k):
    people = [i for i in range(1, n+1)]
    answer = []
    k -= 1
    while len(answer) < n:
        i = len(answer) + 1
        fact = factorial(n-i)
        quotient = k // fact
        k %= fact
        answer.append(people[quotient])
        people.remove(people[quotient])
    return answer