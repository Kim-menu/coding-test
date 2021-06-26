from itertools import permutations


def is_in(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i] and str2[i] != '*':
                return False
        return True
    else:
        return False


def solution(user_id, banned_id):
    total = list(permutations(user_id, len(banned_id)))
    answer_list = []
    for each_case in total:
        case_bool = True
        for i in range(len(banned_id)):
            if not is_in(each_case[i], banned_id[i]):
                case_bool = False
                break
        if case_bool == True:
            temp_list = list(each_case)
            temp_list.sort()
            if temp_list not in answer_list:
                answer_list.append(temp_list)

    answer = len(answer_list)
    return answer