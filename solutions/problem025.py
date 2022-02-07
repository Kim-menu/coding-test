def insert_node(tree, tree_idx, node):
    idx = tree_idx
    while True:
        if tree[idx][0] > node[0]:
            if tree[idx][3] == -1:
                tree.append(node + [-1, -1])
                tree[idx][3] = len(tree) - 1
                break
            else:
                idx = tree[idx][3]
                continue
        else:
            if tree[idx][4] == -1:
                tree.append(node + [-1, -1])
                tree[idx][4] = len(tree) - 1
                break
            else:
                idx = tree[idx][4]
                continue


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i)  # nodeinfo에 node_idx(name)을 저장한다.
    nodeinfo.sort(key=lambda x: x[1], reverse=True)  # 높이 순 정렬
    tree = [nodeinfo[0] + [-1, -1]]  # left, right의 tree idx 추가
    for i in range(1, len(nodeinfo)):  # root 이후부터 tree에 삽입
        insert_node(tree, 0, nodeinfo[i])
    preorder = []
    postorder = []
    my_stack = [0]
    while my_stack:
        tree_idx = my_stack.pop()
        preorder.append(tree[tree_idx][2] + 1)
        if tree[tree_idx][4] != -1:
            my_stack.append(tree[tree_idx][4])
        if tree[tree_idx][3] != -1:
            my_stack.append(tree[tree_idx][3])
    my_stack = [0]
    while my_stack:
        tree_idx = my_stack.pop()
        if tree[tree_idx][3] != -1:
            my_stack.append(tree[tree_idx][3])
        if tree[tree_idx][4] != -1:
            my_stack.append(tree[tree_idx][4])
        postorder.append(tree[tree_idx][2] + 1)
    postorder.reverse()
    answer = [preorder, postorder]
    return answer