#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n0 = 0, n1=0;
	string s;
	cin >> s;
	for (int i = 0; i < s.length(); i++)
	{
		if (i == 0)
		{
			if (s[i]=='0')
			{
				n0++;
			}
			else{
				n1++;
			}
		}
		else {
			if (s[i-1]!= s[i])
			{
				if (s[i-1] == '0')
				{
					n1++;
				}
				else {
					n0++;
				}
			}

		}
	}
	if (n0<n1)
	{
		cout << n0;
	}
	else {
		cout << n1;
	}
	return 0;
}