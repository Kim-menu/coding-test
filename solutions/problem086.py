N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort()


def simulation(x):
    global C
    remain_router = C
    last_router = -int(1e9)
    for i in range(N):
        cur_distance = house[i] - last_router 
        if cur_distance >= x:
            remain_router -= 1
            last_router = house[i]
    if remain_router > 0:
        return False
    else:
        return True


left, right = 1, int(1e9)
while left < right:
    middle = (left + right + 1) // 2
    if simulation(middle):
        left = middle
    else:
        right = middle - 1
print(left)