#include<iostream>
using namespace std;
int main() {
	string str;

	cin >> str;
	for (int i = 0; i < str.length(); i++)
	{
		if (65 <= str[i] && str[i] <= 90) {
			str[i] = str[i] + 32;
		}
		else if (97 <= str[i] && str[i] <= 122) {
			str[i] = str[i] - 32;
		}
	}
	cout << str;
	return 0;
}