#include<iostream>
#include<string>
#include<cmath>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s1,s2;
	long long temp = 0;
	long long result = 0;
	int arr[60] = {0,};
	int n = 0;
	cin >> s1;
	cin >> s2;

	for (int i = 0; i < s2.length(); i++)
	{
		for (int j = 0; j < s1.length(); j++)
		{
			temp += (s1[s1.length()- 1 -j] - 48) * (s2[s2.length() - 1 - i] - 48) * pow(2,j);
		}
		temp *= pow(2, i);
		result += temp;
		temp = 0;
	}
	
	while (result / 2 != 0)
	{
		arr[n] = result % 2;
		n++;
		result /= 2;
	}
	
	arr[n] = result % 2;

	for (int i = n; i >= 0; i--)
	{
		cout << arr[i];
	}

	return 0;
	
}