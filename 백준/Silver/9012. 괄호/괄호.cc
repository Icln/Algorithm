#include <iostream>
#include <stack>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	int T;
	string s;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		stack <char> vps;
		cin >> s;
		for (int j = 0; j < s.length(); j++)
		{
			vps.push(s[j]);
		}
		int cnt = 0;
		int size = vps.size();
		int k = 0;
		for (k = 0; k < size; k++)
		{
			if (vps.top() == '(') {
				if (cnt > 0) {
					cnt--;
					vps.pop();
				}
				else {
					cout << "NO" << '\n';
					break;
				}
			}
			else if (vps.top() == ')')
			{
				if (cnt < 0)
				{
					cout << "NO" << '\n';
					break;
				}
				else {
					cnt++;
					vps.pop();
				}

			}
		}
		if (k == size)
		{
			if (cnt > 0)
			{
				cout << "NO" << '\n';
			}
			else {
				cout << "YES" << '\n';
			}
		}
	}
	return 0;
}