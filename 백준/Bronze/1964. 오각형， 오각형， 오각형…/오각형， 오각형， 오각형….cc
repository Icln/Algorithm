#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	
	int n;
	long long result = 5;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		if (i!=1)
		{
			result += (3*i+1);
		}
	}
	cout << result % 45678;

}