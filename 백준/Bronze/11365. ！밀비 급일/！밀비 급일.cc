#include<iostream>
#include<string>
using namespace std;
int main() {
	string s;
	char arr[500];
	while (true)
	{
		getline(cin, s);
		if (s[0]==69 && s[1]==78 && s[2]==68) {
			return 0;
		}
		for (int i = 0; i < s.length(); i++)
		{
			arr[i] = s[s.length() - 1 - i];
			cout << arr[i];
		}
		cout << endl;
	}
	return 0;
}