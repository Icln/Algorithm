#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector <int>  v;
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
	int n, tree;
	int result = 0;
	int idx = 0;
	
	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> tree;
		v.push_back(tree);
	}
	sort(v.begin(), v.end());
	
	int min = gcd(v[1] - v[0], v[2] - v[1]);
	
	for (int i = 3; i < n; i++){
		min = gcd(min, v[i] - v[i - 1]);
	}

	for (int i = v[0]; i < v[n-1]; i+=min){
		if (v[idx] == i){
			idx++;
		}
		else {
			result++;
		}
	}
	
	cout << result << "\n";

	return 0;
}