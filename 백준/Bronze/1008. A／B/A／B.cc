#include<iostream>
using namespace std;
int main() {
	double a, b;
	cin >> a >> b;
	if (a > 0 && b < 10) {
		double temp = a / b;
		cout << fixed;
		cout.precision(10);
		cout << temp <<	endl;

	}
	else
		cout << "error" << endl;
	return 0;
}