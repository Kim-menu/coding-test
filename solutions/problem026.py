import sys
sys.setrecursionlimit(300000)

answer = 0

def dfs(adjacent, cur_node, visited, a):
    global answer
    for each_node in adjacent[cur_node]:
        if not visited[each_node]:
            visited[each_node] = 1
            result = dfs(adjacent, each_node, visited, a)
            a[cur_node] += result
            answer += abs(result)
    return a[cur_node]

def solution(a, edges):
    if sum(a):
        return -1
    visited = [0]*len(a)
    adjacent = [[] for _ in range(len(a))]
    for [x, y] in edges:
        adjacent[x].append(y)
        adjacent[y].append(x)
    visited[0] = 1
    dfs(adjacent, 0, visited, a)
    return answer