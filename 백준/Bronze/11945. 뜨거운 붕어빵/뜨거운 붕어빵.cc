#include<iostream>
using namespace std;
int main() {
	int n, m;
	char temp;
	cin >> n >> m;
	
	int** arr = new int* [n];
	for (int i = 0; i < n; i++)
	{
		arr[i] = new int[m];
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> temp;
			arr[i][j] = temp-'0';
		}
	}
	
	for (int i = 0; i < n; i++)
	{
		for (int j = m-1; j >= 0; j--)
		{
			cout << arr[i][j];
		}
		cout << endl;
	}

	for (int i = 0; i < n; i++)
	{
		delete[] arr[i];
	}
	delete[] arr;

	return 0;
}