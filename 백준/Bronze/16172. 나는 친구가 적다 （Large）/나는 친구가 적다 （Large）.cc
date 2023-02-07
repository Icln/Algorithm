#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s, k, temp;
	cin >> temp;
	for (const auto &c : temp)
	{
		if ('0' <= c && c <= '9')continue;
		s.push_back(c);
	}
	cin >> k;
	cout << (s.find(k) != string::npos);
	return 0;
	
}