#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
vector<int> arr;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, m;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> m;
		arr.push_back(m);
	}
	sort(arr.begin(), arr.end());
	for (int i = 0; i < arr.size(); i++)
	{
		cout << arr[i] << "\n";
	}
	return 0;
}