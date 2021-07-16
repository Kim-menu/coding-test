def solution(s):
    answer = []
    for each_string in s:
        if len(each_string) < 4:
            answer.append(each_string)
            continue
        stack = list(each_string)
        new_stack = []
        dummy = ""
        for char in stack:
            if char == '0':
                if len(new_stack) >= 2 and new_stack[-2] == '1' and new_stack[-1] == '1':
                    new_stack.pop()
                    new_stack.pop()
                    dummy += "110" #이거 오래걸리나?
                else:
                    new_stack.append('0')
            else:
                new_stack.append('1')
        cursor = 0
        input_idx = -1
        while cursor < len(new_stack)-1:
            if (new_stack[cursor], new_stack[cursor+1]) == ('1', '1'):
                input_idx = cursor
                break
            cursor += 1
        if input_idx == -1 and len(new_stack) > 1 and (new_stack[len(new_stack)-2], new_stack[len(new_stack)-1]) == ('0', '1'):
            input_idx = len(new_stack)-1
        if input_idx == -1 and len(new_stack) == 1 and new_stack[0] == '1':
            input_idx = 0
        if input_idx == -1:
            input_idx = len(new_stack)
        new_stack = new_stack[:input_idx] + [dummy] + new_stack[input_idx:]
        answer.append("".join(new_stack))
    return answer