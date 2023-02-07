#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
vector<pair<int, int>> v;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, m1,m2;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> m1 >> m2;
		v.push_back({ m1,m2 });
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < n; i++)
	{
		cout << v[i].first << ' ' << v[i].second << "\n";
	}
	return 0;
}