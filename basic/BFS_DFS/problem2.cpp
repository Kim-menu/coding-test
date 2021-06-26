# 1. 선택 정렬
# 2. 삽입 정렬
# 3. 퀵 정렬
# 4. 계수 정렬
# 5. 병합 정렬

myList = [3, 6, 4, 7, 8, 0, 2]

def sel_sort(arg_list):
    for i in range(len(arg_list)):
        min = arg_list[i]
        min_idx = i
        for j in range(i, len(arg_list)):
            if arg_list[j] < min:
                min = arg_list[j]
                min_idx = j
        arg_list[min_idx] = arg_list[i]
        arg_list[i] = min


def ins_sort(arg_list):
    for i in range(1, len(arg_list)):
        for j in range(i):
            if arg_list[j] > arg_list[i]:
                temp = arg_list[i]
                for k in range(i, j, -1):
                    arg_list[k] = arg_list[k-1]
                arg_list[j] = temp
                break


def q_sort(arg_list):
    if len(arg_list) == 1: return arg_list
    pivot = 0
    left = 1
    right = len(arg_list)-1
    while True:
        while arg_list[right] > arg_list[pivot]:
            right -= 1
            if right == pivot: return [arg_list[pivot]] + q_sort(arg_list[1:])
        while arg_list[left] < arg_list[pivot]:
            left += 1
            if left == len(arg_list): return q_sort(arg_list[:left]) + [arg_list[pivot]]
        if right < left:
            temp = arg_list[right]
            arg_list[right] = arg_list[pivot]
            arg_list[pivot] = temp
            return q_sort(arg_list[:right]) + [arg_list[right]] + q_sort(arg_list[right+1:])
        else:
            temp = arg_list[left]
            arg_list[left] = arg_list[right]
            arg_list[right] = temp


def count_sort(arg_list):
    count_elem = [0] * (max(arg_list) + 1)
    for elem in arg_list:
        count_elem[elem] += 1
    ret_list = []
    for i in range(len(count_elem)):
        for _ in range(count_elem[i]):
            ret_list.append(i)
    return ret_list


def merge_sort(arg_list):
    if len(arg_list) == 1:
        return arg_list
    middle = (len(arg_list) + 1) // 2
    left_list = merge_sort(arg_list[0:middle])
    right_list = merge_sort(arg_list[middle:])
    new_list = []
    left_cursor = 0
    right_cursor = 0
    while len(new_list) < len(left_list) + len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            new_list.append(left_list[left_cursor])
            left_cursor += 1
        else:
            new_list.append(right_list[right_cursor])
            right_cursor += 1
        if left_cursor == len(left_list): new_list = new_list + right_list[right_cursor:]
        if right_cursor == len(right_list): new_list = new_list + left_list[left_cursor:]
    return new_list
