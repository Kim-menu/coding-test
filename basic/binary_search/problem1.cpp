from bisect import bisect_left, bisect_right

N, x = map(int, input().split())

sequence = list(map(int, input().split()))

x_count = bisect_right(sequence, x) - bisect_left(sequence, x)
if x_count == 0 : x_count = -1
print(x_count)