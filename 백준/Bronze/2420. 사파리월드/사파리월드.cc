#include<iostream>
using namespace std;
int main() {
	long long a, b;
	cin >> a >> b;
	if (a >= -2000000000 && b <= 2000000000){
		if (a < b)
		{
			cout << -1 * (a - b) << endl;
		}
		else {
			cout << a - b << endl;
		}
	}
	else {
		cout << "error" << endl;
	}

	return 0;
}