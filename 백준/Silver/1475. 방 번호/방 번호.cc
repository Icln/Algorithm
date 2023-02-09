#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	
	string s;
	cin >> s;
	int arr[9]= {0,};
	int max = 0;
	for (int i = 0; i <s.length(); i++)
	{
		if (s[i]=='9')
		{
			arr[6]++;
		}
		else {
			arr[s[i] - '0']++;
		}
	}

	for (int i = 0; i < 9; i++)
	{
		if (max < arr[i])
		{
			if (i == 6)
			{
				if (arr[i]%2 == 0)
				{
					max = arr[i] / 2;
				}
				else {
					max = arr[i] / 2 + 1;
				}
			}
			else
				max = arr[i];
		}
	}
	cout << max;
	return 0;
}