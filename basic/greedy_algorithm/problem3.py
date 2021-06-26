N = int(input())
Fear = list(map(int, input().split()))
Fear.sort()
Group = 0
members = 0
for cur_fear in Fear:
    members += 1
    if cur_fear <= members:
        Group += 1
        members = 0

print(Group)
