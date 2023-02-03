#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	
	int n;
	int temp;
	cin >> n;

	int* arr = new int[n];

	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		arr[i] = temp;
	}

	sort(arr, arr + n);
	for (int  i = 0; i < n; i++)
	{
		cout << arr[i] << "\n";
	}
}