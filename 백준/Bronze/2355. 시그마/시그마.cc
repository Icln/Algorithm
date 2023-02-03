#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	
	long long a, b;
	long long result = 0;
	cin >> a >> b;
	if (a < b) {
		result = (b - a + 1) * (a + b) / 2;
	}
	else{
		result = (a - b + 1) * (a + b) / 2;
	}
	cout << result;
	return 0;
}