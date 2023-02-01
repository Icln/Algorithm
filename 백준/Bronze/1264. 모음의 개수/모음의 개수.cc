#include<iostream>
#include<string>
using namespace std;
int main() {
	string s;
	int n = 0;
	while (true)
	{
		getline(cin, s);
		if (s[0]==35) {
			return 0;
		}
		else {
			for (int i = 0; i < s.length(); i++)
			{
				if (s[i] == 65 || s[i] == 69 || s[i] == 73 || s[i] == 79 || s[i] == 85
					|| s[i] == 97 || s[i] == 101 || s[i] == 105 || s[i] == 111 || s[i] == 117) {
					n++;
				}
			}
			cout << n<< endl;
			n = 0;
		}
		
	}
	
	return 0;
}