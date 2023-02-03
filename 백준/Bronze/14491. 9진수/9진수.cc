#include<iostream>
#include<cmath>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	cin >> n;

	int result = 0;
	int arr[5] = {0,};
	int temp = 4;
	while (n / 9 != 0)
	{
		arr[temp] = n % 9;
		temp--;
		n /= 9;
	}
	arr[temp] = n % 9;
	
	int j = 0;
	for (int i = 4; i >= 0; i--)
	{
		result += arr[j] * pow(10,i);
		j++;
	}
		cout << result;
	return 0;
	
}