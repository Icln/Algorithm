#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector <pair<int, int>>  v;
int gcd(int a, int b) {
	int n;

	while (b != 0) {
		n = a % b;
		a = b;
		b = n;
	}

	return a;
}
int lcm(int a, int b) {
	return a * b / gcd(a, b);
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int T, A, B;
	cin >> T;
	for (int i = 0; i < T; i++){
		cin >> A >> B;
		v.push_back({A , B});
	}
	for (int i = 0; i < T; i++)
	{
		cout<< lcm(v[i].first,v[i].second)<<'\n';
	}
	return 0;
}