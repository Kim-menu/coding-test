n = int(input())
sequence = list(map(int, input().split()))
x = int(input())

sequence.sort()
left = 0
right = len(sequence)-1

count = 0

while left < right:
    cur_sum = sequence[left] + sequence[right]
    if cur_sum == x:
        count += 1
        left += 1
    elif cur_sum < x:
        left += 1
    else:
        right -= 1

print(count)