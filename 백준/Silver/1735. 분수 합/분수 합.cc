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
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int A, B;
	int result_a, result_b;
	for (int i = 0; i < 2; i++){
		cin >> A >> B;
		v.push_back({A , B});
	}
	
	result_a = v[0].first * v[1].second + v[1].first * v[0].second;
	result_b = v[0].second * v[1].second;	
	int temp = gcd(result_a, result_b);

	cout << result_a / temp << " " << result_b / temp << " "<<"\n";
	

	return 0;
}