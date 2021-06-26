#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int X;
	cin >> X;
	int *optimum = new int[X+1];
	vector<int> cases;
	int min;

	optimum[1] = 0;
	for (int i = 2; i <= X; i++) {
		min = X;
		if (i % 5 == 0) cases.push_back(optimum[i / 5]);
		if (i % 3 == 0) cases.push_back(optimum[i / 3]);
		if (i % 2 == 0) cases.push_back(optimum[i / 2]);
		cases.push_back(optimum[i - 1]);
		for (int elem : cases)
			min = min > elem ? elem : min;
		optimum[i] = 1 + min;
		cases.clear();
	}
	cout << optimum[X];

	return 0;
}