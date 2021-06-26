# include <bits/stdc++.h>

using
namespace
std;

vector < int > ddeok_vector;

int
cut_length(int
h) {
    int
sum = 0;
for (int i: ddeok_vector)
{
if (h < i)
sum += i - h;
}
return sum;
}

int
binary_search(int
start, int
end, int
value) {
if (end - start == 1) {
if (cut_length(end) < value)
return start;
else return end;
}
int
middle = (start + end) / 2;
if (cut_length(middle) < value)
return binary_search(start, middle - 1, value);
else if (cut_length(middle) > value)
    return binary_search(middle, end, value);
else return middle;
}

int
main(void)
{
int
N, M;
int
temp;
int
max = -1;
cin >> N >> M;

for (int i = 0; i < N; i++) {
    scanf_s("%d", & temp);
ddeok_vector.push_back(temp);
if (max < temp) max = temp;
}

cout << binary_search(0, max, M);

return 0;
}