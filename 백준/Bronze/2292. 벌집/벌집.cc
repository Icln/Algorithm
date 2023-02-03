#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	
	int n;
	int temp = 0;
	int result = 1;
	cin >> n;

	for (int i = 1; i < n; i+=(6*temp))
	{
		result++;
		temp++;
	}
	cout << result;

}