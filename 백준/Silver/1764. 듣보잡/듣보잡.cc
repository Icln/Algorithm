#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, m;
	string s;
	map <string, int> mm;
	vector<string> v;
	cin >> n >> m;
	
	for (int i = 0; i < n + m; i++)
	{
		cin >> s;
		mm[s]++;
		if (mm[s] > 1)
			v.push_back(s);
	}

	sort(v.begin(), v.end());
	cout << v.size() << '\n';
	for (auto i : v)
	{
		cout << i << '\n';
	}
	return 0;
}