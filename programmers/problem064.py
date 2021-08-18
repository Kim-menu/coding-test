import math


def solution(brown, yellow):
    p = (brown+4) / 2
    q = 4*brown + 4*yellow
    h = (p - math.sqrt(p**2 - q))/2
    v = (brown - 2*h + 4)/2
    answer = [int(v), int(h)]
    return answer