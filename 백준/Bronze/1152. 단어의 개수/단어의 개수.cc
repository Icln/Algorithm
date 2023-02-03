#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s;
	int num = 0;
	getline(cin, s);

	for (int i = 0; i < s.length(); i++)
	{
		if (s[i]==' ') {
			num++;
		}
	}
	if (s[0]==' '){
		num--;
	}
	if (s[s.length() - 1] == ' ') {
		num--;
	}
	cout << num + 1;
	return 0;
}