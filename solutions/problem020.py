def solution(genres, plays):
    genres_dict = dict()
    genres_play_num = []
    for i in range(len(genres)):
        if genres[i] in genres_dict.keys():
            genres_dict[genres[i]].append((plays[i], i))
        else:
            genres_dict[genres[i]] = [(plays[i], i)]
    for each_genre in genres_dict.keys():
        genres_dict[each_genre].sort(key = lambda x: x[0], reverse = True)
        sum_play = 0
        for each_play in genres_dict[each_genre]:
            sum_play += each_play[0]
        genres_play_num.append((sum_play, each_genre))
    genres_play_num.sort(key = lambda x: x[0], reverse = True)
    answer = []
    for (play_num, genre) in genres_play_num:
        num = 0
        for (each_play, idx) in genres_dict[genre]:
            if num < 2:
                answer.append(idx)
                num += 1
    return answer