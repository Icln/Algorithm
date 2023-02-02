#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	string s;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> s;
		cout << "String #" << i + 1 << "\n";
		for (int j = 0; j < s.length(); j++)
		{
			if (s[j] == 'Z') {
				cout << 'A';
			}
			else {
				cout << (char)(s[j] + 1);
			}
		}
		cout << "\n" << "\n";
	}
	
	return 0;
}