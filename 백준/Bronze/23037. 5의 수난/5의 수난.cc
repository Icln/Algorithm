#include<iostream>
#include<string>
#include<cmath>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s;
	int tmp = 0;
	cin >> s;
	for (int i = 0; i < s.length(); i++)
	{
		tmp += pow(s[i] - '0', 5);
	}
	cout << tmp;
	return 0;
}