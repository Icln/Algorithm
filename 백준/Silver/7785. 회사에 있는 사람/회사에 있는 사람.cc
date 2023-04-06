#include<iostream>
#include<string>
#include<set>
using namespace std;
int n;
string name, record;
set <string> s;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> name >> record;
		if (record == "enter")
		{
			s.insert(name);
		}
		else {
			s.erase(name);
		}
	}
	
	for (auto it = s.rbegin(); it != s.rend(); it++)
	{
		cout << *it << '\n';
	}
	return 0;
}