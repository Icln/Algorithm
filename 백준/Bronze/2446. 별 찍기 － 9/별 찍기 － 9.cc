#include<iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		for (int k = 0; k < i; k++)
		{
			cout << " ";
		}
		for (int j = n - i; j > 0; j--)
		{
			cout << "*";
		}
		for (int h = n - 1 - i; h > 0; h--)
		{
			cout << "*";
		}
		cout << endl;
	}

	for (int i = 1; i < n; i++)
	{
		for (int j = n - 1 -i; j > 0; j--)
		{
			cout << " ";
		}
		for (int k = 0; k <= i; k++)
		{
			cout << "*";
		}
		for (int h = 0; h < i; h++)
		{
			cout << "*";
		}
		cout << endl;
	}

	return 0;
}