#include <bits/stdc++.h>

using namespace std;

int main(void) {
	stack<int> myStack;

	myStack.push(0);
	myStack.push(2);
	myStack.pop();

	while (!myStack.empty()) {
		cout << myStack.top() << ' ';
		myStack.pop();
	}
	return 0;

}