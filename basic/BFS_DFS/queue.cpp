N, M = map(int, input().split())

iceTray = []

for _ in range(N):
    iceTray.append(list(map(int, input())))

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
stack = []
Traverse = set()
count = 0
for x in range(N):
    for y in range(M):
        if (x, y) not in Traverse and iceTray[x][y] == 0:
            count += 1
        stack.append((x, y))
        while len(stack) != 0:
            (pop_x, pop_y) = stack.pop()

            if (pop_x, pop_y) in Traverse: continue

            Traverse.add((pop_x, pop_y))
            if iceTray[pop_x][pop_y] == 1:
                continue
            else:
                for i in range(len(dx)):
                    (next_x, next_y) = (pop_x + dx[i], pop_y + dy[i])
                    if 0 <= next_x < N and 0 <= next_y < M:
                        stack.append((next_x, next_y))
print(count)