N, K = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)
sum = 0
swap_count = 0

for i in range(N):
    if swap_count < K and a_list[i] < b_list[i]:
        sum += b_list[i]
        swap_count += 1
    else:
        sum += a_list[i]

print(sum)