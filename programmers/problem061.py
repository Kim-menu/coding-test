from itertools import permutations
import math


def isPrime(n):
    if n <= 1:
        return 0
    up_sqrt = int(math.sqrt(n)) + 1
    for i in range(2, up_sqrt):
        if n % i == 0:
            return 0
    return 1


def solution(numbers):
    answer = 0
    num_list = [digit for digit in numbers]
    total_case = set()
    for i in range(1, len(num_list)+1):
        for char_list in permutations(numbers, i):
            num_str = ''.join(char_list)
            total_case.add(int(num_str))
    for num in total_case:
        if isPrime(num):
            answer += 1
    return answer