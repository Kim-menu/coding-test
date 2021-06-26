#include <bits/stdc++.h>

using namespace std;

int main(void) {
	queue<int> myQ;

	myQ.push(3);
	myQ.push(4);

	while (!myQ.empty()) {
		cout << myQ.front() << ' ';
		myQ.pop();
	}
	return 0;

}