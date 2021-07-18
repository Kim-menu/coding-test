def score(word, body):
    start_idx = 0
    count = 0
    while body[start_idx:].find(word) >= 0:
        start_idx = body[start_idx:].find(word) + start_idx
        if start_idx > 0 and 'a' <= body[start_idx - 1] <= 'z':  # 일치 단어 맞는지 (앞뒤 알파벳 여부 검사)
            start_idx += 1
            continue
        if start_idx + len(word) < len(body) and 'a' <= body[start_idx + len(word)] <= 'z':
            start_idx += 1
            continue
        count += 1
        start_idx += 1
    return count


def solution(word, pages):
    parsed_pages = []  # page html에서 필요한 정보만 parse한 Dict들의 list
    idx_dict = dict()  # 각 url(key)이 몇번째 idx(val)인지 저장함
    for i, page in enumerate(pages):
        cur_dict = dict()  # 지금 page를 parsing할 dict 생성

        start_idx = 0
        while page[start_idx:].find("<meta") >= 0: # url값 추출
            start_idx = page[start_idx:].find("<meta") + start_idx
            end_idx = page[start_idx:].find('>') + start_idx
            if page[start_idx:end_idx].find("content=\"https://") >= 0:
                start_idx = page[start_idx:].find("content=\"https://") + start_idx + 9
                break
            start_idx += 1
        end_idx = page[start_idx:].find('\"') + start_idx - 1
        cur_dict["url"] = page[start_idx:end_idx + 1]
        idx_dict[cur_dict["url"]] = i

        cur_dict["body"] = page.lower()

        end_idx = 0
        while page[end_idx:].find("<a href=") > 0:  # link죄다 추출
            start_idx = page[end_idx:].find("<a href=") + end_idx
            start_idx = page[start_idx:].find("https://") + start_idx
            end_idx = page[start_idx:].find('\"') + start_idx - 1
            if "links" in cur_dict.keys():
                cur_dict["links"].append(page[start_idx:end_idx + 1])
            else:
                cur_dict["links"] = [page[start_idx:end_idx + 1]]

        cur_dict["basic_score"] = score(word.lower(), cur_dict["body"])
        cur_dict["link_score"] = 0
        parsed_pages.append(cur_dict)

    for i, cur_dict in enumerate(parsed_pages):
        if "links" in cur_dict.keys():
            for link in cur_dict["links"]:
                if link in idx_dict.keys():
                    parsed_pages[idx_dict[link]]["link_score"] += cur_dict["basic_score"] / len(cur_dict["links"])

    score_list = []
    for i, cur_dict in enumerate(parsed_pages):
        score_list.append((cur_dict["basic_score"] + cur_dict["link_score"], i))
    score_list.sort(key = lambda x : -x[0])

    answer = score_list[0][1]
    return answer