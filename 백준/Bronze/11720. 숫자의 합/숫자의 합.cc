#include<iostream>
#include<string>
using namespace std;
int main() {
	string s;
	int l;
	int num = 0;
	cin >> l;
	cin >> s;
	
	if (s.length() >= 1 && s.length() <= 100) {
		for (int i = 0; i < s.length(); i++)
		{
			num += (s[i] - '0');
		}
		cout << num << endl;
	}
	else {
		cout << "error" << endl;
	}
	return 0;
}