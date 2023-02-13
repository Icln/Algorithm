#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v1;
vector<int> v2;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	int tmp;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		v1.push_back(tmp);
		v2.push_back(tmp);
	}
	
	sort(v1.begin(), v1.end());
	v1.erase(unique(v1.begin(),v1.end()), v1.end());
	for (int i = 0; i < n; i++)
	{
		cout<<lower_bound(v1.begin(), v1.end(), v2[i]) - v1.begin()<<' ';
	}
	return 0;
}