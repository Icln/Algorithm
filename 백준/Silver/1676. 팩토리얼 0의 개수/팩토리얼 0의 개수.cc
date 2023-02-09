#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	int result = 0;
	cin >> n;
	for (int i = 5; i <= n; i*=5)
	{
		result += n / i;
	}
	cout << result;
	return 0;
}