#include<iostream>
#include<string>
using namespace std;
int arr[26];
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	int result;
	string s;
	cin >> n;
	result = n;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		for (int j = 0; j < s.length(); j++)
		{
			if (j == 0)
			{
				arr[s[j] - 'a']++;
			}
			else {
				if (s[j-1] != s[j])
				{
					arr[s[j] - 'a']++;
				}
			}
		}
		for (int k = 0; k < 26; k++)
		{
			if (arr[k]>1)
			{
				result--;
				break;
			}
		}
		for (int o = 0; o < 26; o++)
		{
			arr[o] = 0;
		}
	}
	cout << result;
	return 0;
}