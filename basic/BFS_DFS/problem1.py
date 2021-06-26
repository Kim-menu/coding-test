#include <bits/stdc++.h>

using namespace std;

int N, M;
int myMap[201][201];
int Path[201][201] = { 0, };
int path = 1;

void bfs() {
	int dx[4] = { 0, 0, 1, -1 };
	int dy[4] = { 1, -1, 0, 0 };
	int cur_x, cur_y;
	int next_x, next_y;
	queue<pair<int, int>> myQueue;
	myQueue.push(pair<int, int>(0, 0));
	Path[0][0] = 1;

	while (!myQueue.empty()) {
		cur_x = myQueue.front().first;
		cur_y = myQueue.front().second;
		myQueue.pop();
		if (cur_x + 1 == N && cur_y + 1 == M) {
			cout << Path[cur_x][cur_y];
            return;
		}
		for (int i = 0; i < 4; i++) {
			next_x = cur_x + dx[i];
			next_y = cur_y + dy[i];
			if (next_x >= 0 && next_x < N && next_y >= 0 && next_y < M && myMap[next_x][next_y] != 0 && Path[next_x][next_y] == 0) {
				myQueue.push(pair<int, int>(next_x, next_y));
				Path[next_x][next_y] = Path[cur_x][cur_y] + 1;
			}
		}
	}
}

int main(void) {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			scanf_s("%1d", &myMap[i][j]);
	}
	bfs();
	return 0;
}
