def Find(root, pos):
    (r, c) = pos
    if root[r][c] == (r, c):
        return (r, c)
    else:
        root[r][c] = Find(root, root[r][c])
        return root[r][c]


def Union(root, pos1, pos2):
    (r1, c1) = Find(root, pos1)
    (r2, c2) = Find(root, pos2)
    if (r1, c1) < (r2, c2):
        root[r2][c2] = root[r1][c1]
    else:
        root[r1][c1] = root[r2][c2]


def mini_find(root, x):
    if x == root[x]:
        return x
    else:
        root[x] = mini_find(root, root[x])
        return root[x]


def mini_union(root, x, y):
    if mini_find(root, x) < mini_find(root, y):
        root[mini_find(root, y)] = mini_find(root, x)
    else:
        root[mini_find(root, x)] = mini_find(root, y)


def kruskal(total_edge, node_count):
    root = [i for i in range(node_count)]
    result = 0
    while total_edge:
        (weight, x, y) = total_edge.pop()
        if mini_find(root, x) != mini_find(root, y):
            result += weight
            mini_union(root, x, y)
        else:
            continue
    return result


def solution(land, height):
    N = len(land)
    root = [[(r, c) for c in range(N)] for r in range(N)]
    for r in range(N - 1):
        for c in range(N):
            if abs(land[r][c] - land[r + 1][c]) <= height:
                Union(root, (r, c), (r + 1, c))
    for c in range(N - 1):
        for r in range(N):
            if abs(land[r][c] - land[r][c + 1]) <= height:
                Union(root, (r, c), (r, c + 1))
    Node_set = set()
    for r in range(N):
        for c in range(N):
            Node_set.add(Find(root, (r, c)))
    Node_idx = dict()
    cur_idx = 0
    for Node in Node_set:
        Node_idx[Node] = cur_idx
        cur_idx += 1
    Edge = dict()
    for r in range(N - 1):
        for c in range(N):
            area1 = Find(root, (r, c))
            area2 = Find(root, (r + 1, c))
            if area1 != area2:
                (start, end) = (min(Node_idx[area1], Node_idx[area2]), max(Node_idx[area1], Node_idx[area2]))
                weight = abs(land[r][c] - land[r + 1][c])
                if (start, end) in Edge.keys():
                    Edge[(start, end)] = min(weight, Edge[(start, end)])
                else:
                    Edge[(start, end)] = weight
    for c in range(N - 1):
        for r in range(N):
            area1 = Find(root, (r, c))
            area2 = Find(root, (r, c + 1))
            if area1 != area2:
                (start, end) = (min(Node_idx[area1], Node_idx[area2]), max(Node_idx[area1], Node_idx[area2]))
                weight = abs(land[r][c] - land[r][c + 1])
                if (start, end) in Edge.keys():
                    Edge[(start, end)] = min(weight, Edge[(start, end)])
                else:
                    Edge[(start, end)] = weight
    total_edge = []
    for (start, end) in Edge.keys():
        total_edge.append((Edge[(start, end)], start, end))
    total_edge.sort(reverse=True)
    answer = kruskal(total_edge, cur_idx)
    return answer
