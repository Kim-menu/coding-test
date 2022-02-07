from collections import deque


def solution(prices):
    inspect = deque([(prices[0], 0)])
    answer = [0]*len(prices)
    for i in range(1, len(prices)):
        start = inspect[0][1]
        next_idx = -1
        while start != next_idx:
            cur_price, cur_idx = inspect.popleft()
            if cur_price > prices[i]:
                answer[cur_idx] = i - cur_idx
            else:
                inspect.append((cur_price, cur_idx))
            if not inspect:
                break
            next_idx = inspect[0][1]
        inspect.append((prices[i], i))
    for price, idx in inspect:
        answer[idx] = len(prices) - idx - 1
    return answer