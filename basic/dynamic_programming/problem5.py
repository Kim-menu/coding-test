import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h):
        result.append(heapq.heappop(h)) # 이때 작은 값부터 나오게 됨
    return result

result = heapsort([1, 5, 0, 7])
print(result) # [0, 1, 5, 7]