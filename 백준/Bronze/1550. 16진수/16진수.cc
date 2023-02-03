#include<iostream>
#include<string>
#include<cmath>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s;
	cin >> s;
	int temp = 0;
	int result = 0;
	for (int i = s.length() - 1; i >= 0; i--)
	{
		if (s[i] >= 65 && s[i] <= 70){
			s[i] -= 55;
		}
		else if (s[i] >= 48 && s[i] <= 57) {
			s[i] -= 48;
		}
		result += (int)s[i] * pow(16, temp);
		temp++;
	}
	cout << result;
	return 0;
}