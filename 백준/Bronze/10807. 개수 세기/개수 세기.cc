#include <iostream>
using namespace std;
int main() {
	int N;
	cin >> N;
	int* a = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> a[i];
	}
	int v;
	cin >> v;
	int count = 0;
	for (int i = 0; i < N; i++) {
		if (a[i] == v) {
			count++;
		}
	}
	cout << count;
}