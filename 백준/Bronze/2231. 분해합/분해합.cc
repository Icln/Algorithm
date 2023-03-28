#include <iostream>
using namespace std;

int find_min(int i) {
	int sum = i;
	while (i > 0)
	{
		sum += i % 10;
		i /= 10;
	}
	return sum;
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	cin >> n;

	for (int i = 1; i < n; i++)
	{
		if (find_min(i) == n) {
			cout << i;
			return 0;
		}
	}

	cout << 0;

	return 0;
}