def cal_money(parent_dict, result_dict, cur_seller, cur_money):
    parent_money = int(0.1 * cur_money)
    my_money = cur_money - parent_money
    result_dict[cur_seller] += my_money
    if parent_dict[cur_seller] == "-" or parent_money == 0:
        return
    else:
        cal_money(parent_dict, result_dict, parent_dict[cur_seller], parent_money)


def solution(enroll, referral, seller, amount):
    parent_dict = dict()
    result_dict = dict()
    for i in range(len(enroll)):
        parent_dict[enroll[i]] = referral[i]
        result_dict[enroll[i]] = 0
    for i in range(len(seller)):
        cal_money(parent_dict, result_dict, seller[i], amount[i] * 100)
    answer = []
    for i in range(len(enroll)):
        answer.append(result_dict[enroll[i]])
    return answer