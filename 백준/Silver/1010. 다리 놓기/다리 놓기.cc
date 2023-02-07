#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int t, n, m;
	long long temp, result;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		result = 1;
		temp = 1;

		cin >> n >> m;
		for (int j = m; j > m -n; j--)
		{
			result *= j;
			result /= temp++;
		}
		cout << result << "\n";
	}
	return 0;
}