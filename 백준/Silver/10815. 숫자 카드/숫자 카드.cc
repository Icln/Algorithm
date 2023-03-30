#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector <bool> v(20000001, false);
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n,tmp;
	
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		v[tmp + 10000000] = true;
	}
	
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		if (v[tmp + 10000000]) cout << "1 ";
		else cout << "0 ";
	}
	
	return 0;
}