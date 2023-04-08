#include <iostream>
using namespace std;
typedef long long ll;

ll N;
ll ans = 1;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (ll i = 2; i <= N; i++) ans *= i;

	cout << ans;
}