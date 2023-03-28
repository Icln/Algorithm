#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector <pair<int, int>>  v;
bool compare(pair<int,int> a, pair<int,int> b) {
	if (a.second == b.second)
	{
		return a.first < b.first;
	}
	else
	{
		return a.second < b.second;
	}
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, x, y;
	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> x >> y;
		v.push_back({x ,y});
	}
	sort(v.begin(), v.end(),compare);
	for (auto i : v)
	{
		cout << i.first << " " << i.second << "\n";
	}

	return 0;
}