#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, m;
	map <string, int> ear;
	map <string, int> eye;
	cin >> n >> m;
	string s;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		ear.insert({s,1});
	}
	for (int i = 0; i < m; i++)
	{
		cin >> s;
		eye.insert({s,1});
	}
	int result = 0;
	vector<string> v;
	for (auto i : eye)
	{
		if (ear.count(i.first)) {
			result++;
			v.push_back(i.first);
		}
	}
	
	cout << result << '\n';
	for (auto i : v)
	{
		cout << i << '\n';
	}
	return 0;
}