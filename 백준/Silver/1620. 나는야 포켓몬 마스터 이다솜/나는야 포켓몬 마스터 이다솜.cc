#include <iostream>
#include <map>
#include <string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, m;
	map <string, int> name;
	map <int, string> idx;
	string s;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		name.insert({s,i+1});
		idx.insert({i+1, s});
	}
	for (int i = 0; i < m; i++)
	{
		cin >> s;
		if (s[0] >= '1' && s[0] <= '9') {
			cout << idx[stoi(s)] << '\n';
		}
		else {
			cout << name[s] << '\n';
		}	
	}
	return 0;
}