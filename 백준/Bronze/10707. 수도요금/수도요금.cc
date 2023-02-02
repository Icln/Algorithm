#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int x;
	int y1, y2, y3;
	int p;
	cin >> x >> y1 >> y2 >> y3 >> p;

	if (y2 < p)
	{
		if ((x * p) > y1 + (y3 * (p - y2))){
			cout << y1 + (y3 * (p - y2)) << "\n";
		}
		else {
			cout << x * p << "\n";
		}
	}
	else
	{
		if ((x * p) > y1) {
			cout << y1 << "\n";
		}
		else {
			cout << x * p << "\n";
		}
	}
	
	return 0;
}