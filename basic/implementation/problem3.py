charX, charY = input()
x = ord(charX) - ord('a') + 1
y = int(charY)
dx = (2, 2, -2, -2, 1, 1, -1, -1)
dy = (1, -1, 1, -1, 2, -2, 2, -2)
caseCount = 0
for i in range(len(dx)):
    nextX = x + dx[i]
    nextY = y + dy[i]
    if 1 <= nextX <= 8 and 1 <= nextY <= 8:
        caseCount += 1
print(caseCount)