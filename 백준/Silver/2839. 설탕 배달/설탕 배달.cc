#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	int result = 0;
	cin >> n;
	while (n>=0) {
		if (n % 5 == 0)
		{
			result += n / 5;
			cout << result;
			return 0;
		}
		result++;
		n -= 3;
	}
	cout << -1;
	return 0;
}