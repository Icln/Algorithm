#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector <int> v;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n,tmp;
	
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		v.push_back(tmp);
	}
	sort(v.begin(), v.end());
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		cout << binary_search(v.begin(), v.end(), tmp)<<' ';
	}
	
	return 0;
}