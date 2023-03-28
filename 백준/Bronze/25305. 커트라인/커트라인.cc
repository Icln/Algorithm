#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, k, x;
	vector <int> v;
	cin >> n >> k;

	for (int i = 0; i < n; i++){
		cin >> x;
		v.push_back(x);
	}
	sort(v.begin(), v.end(),greater<int>());
	cout << v[k - 1]<<'\n';
	return 0;
}