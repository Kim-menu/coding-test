N = int(input())
Plan = tuple(input().split())
Update = {
    'R' : (0, 1),
    'L' : (0, -1),
    'U' : (-1, 0),
    'D' : (1, 0)
}
curPos = [1, 1]
for direction in Plan:
    next_x = curPos[0] + Update[direction][0]
    next_y = curPos[1] + Update[direction][1]
    if 1 <= next_x <= N:
        curPos[0] = next_x
    if 1 <= next_y <= N:
        curPos[1] = next_y
print(curPos[0], curPos[1])