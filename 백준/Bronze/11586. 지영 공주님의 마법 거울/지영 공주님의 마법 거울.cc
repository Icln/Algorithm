#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int x;
	int n;
	cin >> x;
	
	char** arr = new char* [x];
	for (int i = 0; i < x; i++)
	{
		arr[i] = new char [x];
	}
	
	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < x; j++)
		{
			cin >> arr[i][j];
		}
	}

	cin >> n;
	switch (n)
	{
	case 1:
		for (int i = 0; i < x; i++)
		{
			for (int j = 0; j < x; j++)
			{
				cout << arr[i][j];
			}
			cout << "\n";
		}
		break;
	case 2:
		for (int i = 0; i < x; i++)
		{
			for (int j = x-1; j >= 0; j--)
			{
				cout << arr[i][j];
			}
			cout << "\n";
		}
		break;
	case 3:
		for (int i = x-1; i >= 0; i--)
		{
			for (int j = 0; j < x; j++)
			{
				cout << arr[i][j];
			}
			cout << "\n";
		}
		break;
	default:
		break;
	}
	return 0;
}