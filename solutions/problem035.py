def check_pd(main_stack, main_top, sub_stack, sub_top):
    result = [1, 1]
    if len(main_stack) == 0:
        pass
    elif len(main_stack) == 1:
        if main_stack[main_top] == sub_stack[sub_top]:
            result[0] = 2
    else:  # main에 2글자 이상 남아있을때
        main_top_case = [main_top, main_top]
        sub_top_case = [sub_top, sub_top]
        if main_stack[main_top - 1] == sub_stack[sub_top]:
            result[0] = 3
            main_top_case[0] -= 1
            while main_top_case[0] * sub_top_case[0] > 0:
                main_top_case[0] -= 1
                sub_top_case[0] -= 1
                if main_stack[main_top_case[0]] == sub_stack[sub_top_case[0]]:
                    result[0] += 2
                else:
                    break
        if main_stack[main_top] == sub_stack[sub_top]:
            result[1] = 2
            while main_top_case[1] * sub_top_case[1] > 0:
                main_top_case[1] -= 1
                sub_top_case[1] -= 1
                if main_stack[main_top_case[1]] == sub_stack[sub_top_case[1]]:
                    result[1] += 2
                else:
                    break
    return max(result)


def solution(s):
    answer = 1
    main_stack = list(s)
    main_stack.reverse()
    main_top = len(main_stack) - 1
    sub_stack = []
    sub_top = -1
    while main_stack:
        cur_char = main_stack.pop()
        main_top -= 1
        sub_stack.append(cur_char)
        sub_top += 1
        answer = max(answer, check_pd(main_stack, main_top, sub_stack, sub_top))

    return answer