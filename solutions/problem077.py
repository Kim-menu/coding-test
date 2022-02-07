class Node:
    def __init__(self, char):
        self.char = char
        self.end_flag = None
        self.children = {}
        self.len_count = {}


def insert(head, word):
    curNode = head
    for i in range(len(word)):
        if len(word)-i in curNode.len_count.keys():
            curNode.len_count[len(word)-i] += 1
        else:
            curNode.len_count[len(word)-i] = 1
        if word[i] not in curNode.children.keys():
            newNode = Node(word[i])
            curNode.children[word[i]] = newNode
        curNode = curNode.children[word[i]]
    curNode.end_flag = True


def find(head, query):
    curNode = head
    for i in range(len(query)):
        if query[i] == '?':
            if len(query)-i in curNode.len_count.keys():
                return curNode.len_count[len(query)-i]
            else:
                return 0
        elif query[i] in curNode.children.keys():
            curNode = curNode.children[query[i]]
        else:
            return 0
    return 0


def solution(words, queries):
    head = Node('')
    rhead = Node('')
    for word in words:
        insert(head, word)
        insert(rhead, word[::-1])
    answer = []
    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            if len(query) not in head.len_count.keys():
                answer.append(0)
            else:
                answer.append(head.len_count[len(query)])
        elif query[-1] == '?':
            answer.append(find(head, query))
        else:
            answer.append(find(rhead, query[::-1]))
    return answer