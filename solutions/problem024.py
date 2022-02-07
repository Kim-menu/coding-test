def find(a, root):
    if root[a] == a: return a
    else:
        root[a] = find(root[a], root)
        return root[a]

def union(a, b, root):
    if find(a, root) == find(b, root): return False # cycle made
    elif find(a, root) < find(b, root):
        root[find(b, root)] = find(a, root)
    else:
        root[find(a, root)] = find(b, root)
    return True

def solution(n, costs):
    root = [i for i in range(n)] #최초 root는 자기 자신들
    costs.sort(key = lambda x: x[2])
    answer = 0
    for [a, b, cost] in costs:
        if not union(a, b, root): continue
        else: answer += cost
    return answer