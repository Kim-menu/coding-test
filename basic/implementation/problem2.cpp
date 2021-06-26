#include <bits/stdc++.h>

using namespace std;

int main(void) {
    string input;
    string output = "";
    vector<char> chars;
    cin >> input;
    int sum = 0;
    for (int i = 0; i < input.size(); i++) {
        if(input[i] > '9') chars.push_back(input[i]);
        else sum += input[i] - '0';
    }
    sort(chars.begin(), chars.end());
    for (int i = 0; i < chars.size(); i++)
        output.append(1, chars.at(i));
    output.append(to_string(sum));
    cout << output;
    return 0;
}
