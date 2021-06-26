def find_root(com, parent):
    if parent[com] != com:
        parent[com] = find_root(parent[com], parent)
        return parent[com]
    else:
        return com


def union_com(a, b, parent):
    root_a = find_root(a, parent)
    root_b = find_root(b, parent)
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b


def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_com(i, j, parent)
    network = set()
    for i in range(n):
        network.add(find_root(i, parent))
    answer = len(network)
    return answer