#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	
	int a, b, c;
	cin >> a >> b >> c;
	if (b>=c){
		cout << -1;
	}
	else {
		cout << a / (c - b) + 1;
	}
	return 0;
}