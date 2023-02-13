#include<iostream>
using namespace std;
int factorial(int n) {
	if (n == 0)
	{
		return 1;
	}
	return n * factorial(n - 1);
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	cin >> n;
	cout<<factorial(n);
	return 0;
}