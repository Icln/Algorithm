#include<iostream>
#include<cmath>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	double d, h, w;
	cin >> d >> h >> w;
	
	double temp = pow(d, 2) / (pow(h, 2) + pow(w, 2));
	cout << (int)floor(sqrt(temp * pow(h, 2))) << " " << (int)floor(sqrt(temp * pow(w, 2)));
	return 0;
}