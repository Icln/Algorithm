#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
vector <string> v;
bool lengthCompare(string a, string b) {
	if (a.length() == b.length())
		return a < b;
	return a.length() < b.length();
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	string s;
	cin >> n;
	for (int  i = 0; i < n; i++)
	{
		cin >> s;
		v.push_back(s);
	}
	sort(v.begin(), v.end(), lengthCompare);
	v.erase(unique(v.begin(), v.end()), v.end());

	for (int i = 0; i < v.size(); i++)
	{
		cout << v[i] << "\n";
	}
	return 0;
}