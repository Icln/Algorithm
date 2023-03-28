#include <iostream>
using namespace std;
long long int gcd(long long int a, long long int b) {
	long long int n;

	while (b != 0) {
		n = a % b;
		a = b;
		b = n;
	}

	return a;
}
long long int lcm(long long int a, long long int b) {
	return a * b / gcd(a, b);
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	long long int A, B;
	cin >> A >> B;
	cout << lcm(A, B) << '\n';

	return 0;
}