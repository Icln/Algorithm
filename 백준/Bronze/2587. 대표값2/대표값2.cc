#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int num, sum =0;
	int arr[5];
	for (int i = 0; i < 5; i++)
	{
		cin >> num;
		sum += num;
		arr[i] = num;
	}

	sort(arr, arr + 5);
	cout << sum / 5<<'\n'<< arr[2];

	return 0;
}