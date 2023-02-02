#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s;
	cin >> s;
	for (int i = 1; i <= s.length(); i++)
	{
		cout << s[i-1];
		if (i % 10 == 0) {
			cout << "\n";
		}
	}
	return 0;
}