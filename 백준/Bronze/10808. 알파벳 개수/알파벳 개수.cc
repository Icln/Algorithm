#include<iostream>
#include<string>
using namespace std;
int main() {
	string s;
	int n[26]={0,};

	cin >> s;

	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] >= 97 && s[i] <= 122) {
			n[s[i] - 'a'] += 1;
		}
		else {
			cout << "error" << endl;
			return 0;
		}
	}

	for (int i = 0; i < 26; i++)
	{
		cout << n[i] << " ";
	}
	
	return 0;
}