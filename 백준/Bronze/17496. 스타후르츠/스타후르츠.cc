#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, t, c, p;
	cin >> n >> t >> c >> p;
	if (n % t == 0)
	{
		cout << (n / t - 1) * c * p;
	}
	else {
		cout << n / t * c * p;
	}
	return 0;
}