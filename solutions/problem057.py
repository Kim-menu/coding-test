def solution(numbers):
    num_str = list(map(str, numbers))
    num_str.sort(key=lambda x: x*3, reverse=True)
    answer = ''
    for n in num_str:
        answer += n
    return str(int(answer))