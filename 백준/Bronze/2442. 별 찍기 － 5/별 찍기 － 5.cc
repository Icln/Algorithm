#include<iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		for (int j = n - 1 - i; j > 0; j--)
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