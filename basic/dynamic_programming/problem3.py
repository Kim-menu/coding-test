#include <bits/stdc++.h>

using namespace std;

int n, m;
int dp[20][20] = { 0, };
int gold[20][20] = { 0, };


int pre_max(int x, int y) {
	vector<int> cases;
	if (x > 0) cases.push_back(dp[x - 1][y - 1]);
	if (x < n - 1) cases.push_back(dp[x + 1][y - 1]);
	cases.push_back(dp[x][y - 1]);
	return *max_element(cases.begin(), cases.end());
}

int main(void) {

	int T;
	cin >> T;
	int* results = new int[T];
	int sol;

	for (int t = 0; t < T; t++) {
		sol = 0;
		cin >> n >> m;
		for (int x = 0; x < n; x++) {
			for (int y = 0; y < m; y++) {
				cin >> gold[x][y];
			}
		}
		for (int x = 0; x < n; x++)
			dp[x][0] = gold[x][0];
		for (int y = 1; y < m; y++) {
			for (int x = 0; x < n; x++) {
				dp[x][y] = gold[x][y] + pre_max(x, y);
				sol = dp[x][y] > sol ? dp[x][y] : sol;
			}
		}
		results[t] = sol;
	}
	for (int t = 0; t < T; t++)
		cout << results[t] << endl;

	delete[] results;

	return 0;
}