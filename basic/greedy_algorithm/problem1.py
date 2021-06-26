N, K = map(int, input().split())
count = 0
while N != 1:
    N = N//K if N%K == 0 else N-1
    count += 1
print(count)