#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int arr[26];
vector<int> v;
bool compare(int a, int b) {
	return b < a;
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s;
	cin >> s;
	for (int i = 0; i < s.length(); i++)
	{
		v.push_back(s[i]-'0');
	}
	sort(v.begin(), v.end(), compare);
	for (const auto &i : v)
	{
		cout << i;
	}
	return 0;
}