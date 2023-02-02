#include<iostream>
using namespace std;
int main() {
	int a, b;
	int n3, n4, n5, n6;
	cin >> a;
	cin >> b;

	if (a / 100 < 10 && a / 100 >= 1 && b / 100 < 10 && b / 100 >= 1)
	{
		n3 = a * (b % 10);
		n4 = a * ((b % 100)/10);
		n5 = a * (b / 100);
		n6 = n3 + (n4 * 10) + (n5 * 100);
		cout << n3 << "\n" << n4 << "\n" << n5 << "\n" << n6 << "\n";
	}
	else {
		cout << "error" << "\n";
	}
	return 0;
}