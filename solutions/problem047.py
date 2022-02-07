def DFS(Queen, cur_row):
    n = len(Queen)
    if cur_row == n:
        return 1
    count = 0
    for col in range(n):
        flag = 0
        Queen[cur_row] = col
        for pre_row in range(cur_row): #이전 row들에 대해서 검사
            if Queen[pre_row] == col: #같은 col 있는지 검사
                flag = 1
                break
            if pre_row - Queen[pre_row] == cur_row - Queen[cur_row]: #대각선1 검사
                flag = 1
                break
            if pre_row + Queen[pre_row] == cur_row + Queen[cur_row]: #대각선2 검사
                flag = 1
                break
        #검사 다 통과 하면
        if flag == 0:
            count += DFS(Queen, cur_row+1)
    return count

def solution(n):
    Queen = [0]*n
    answer = DFS(Queen, 0)
    return answer