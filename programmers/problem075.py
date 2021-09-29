def calc(op1, op2, operator):
    if operator == "+":
        return int(op1) + int(op2)
    else:
        return int(op1) - int(op2)


def minmax(min_result, max_result, arr, start, end):
    if min_result[start][end] != int(1e9):
        return (min_result[start][end], max_result[start][end])
    start_pos = 2 * start
    end_pos = 2 * end
    if end == start:
        return (arr[start_pos], arr[start_pos])
    elif end - start == 1:
        return (
        calc(arr[start_pos], arr[end_pos], arr[start_pos + 1]), calc(arr[start_pos], arr[end_pos], arr[start_pos + 1]))
    else:
        candidate = []
        for i in range(start, end):
            operator_pos = 2 * i + 1
            front = minmax(min_result, max_result, arr, start, i)
            rear = minmax(min_result, max_result, arr, i + 1, end)
            if arr[operator_pos] == "-":
                candidate.append(int(front[1]) - int(rear[0]))  # max
                candidate.append(int(front[0]) - int(rear[1]))  # min
            else:
                candidate.append(int(front[1]) + int(rear[1]))  # max
                candidate.append(int(front[0]) + int(rear[0]))  # min
        min_result[start][end] = min(candidate)
        max_result[start][end] = max(candidate)
        return (min_result[start][end], max_result[start][end])


def solution(arr):
    operand_num = len(arr) // 2 + 1
    min_result = [[int(1e9)]*operand_num for _ in range(operand_num)]
    max_result = [[-int(1e9)]*operand_num for _ in range(operand_num)]
    answer = minmax(min_result, max_result, arr, 0, operand_num - 1)[1]
    return answer