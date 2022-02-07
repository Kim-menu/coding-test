def solution(weights, head2head):
    player_data = []
    for i in range(len(head2head)):
        total_match = 0
        win_match = 0
        win_overweight = 0
        for j in range(len(head2head)):
            if head2head[i][j] == "W":
                total_match += 1
                win_match += 1
                if weights[i] < weights[j]:
                    win_overweight += 1
            elif head2head[i][j] == "L":
                total_match += 1
        if total_match == 0:
            total_match = 1
        win_rate = win_match / total_match
        player_data.append((win_rate, win_overweight, weights[i], -i))
    player_data.sort(reverse=True)
    answer = [1-data[3] for data in player_data]
    return answer