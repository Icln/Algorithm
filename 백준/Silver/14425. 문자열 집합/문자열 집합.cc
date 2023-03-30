#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector <string> v;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, m;
	int result = 0;
	string s;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		v.push_back(s);
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < m; i++)
	{
		cin >> s;
		if (binary_search(v.begin(), v.end(), s)) {
			result++;
		}
	}
	cout << result ;
	return 0;
}