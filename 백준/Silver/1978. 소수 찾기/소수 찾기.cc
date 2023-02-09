#include<iostream>
#include<vector>
using namespace std;
vector<int> v;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n,x;
	int result = 0;
	int tmp = 0;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		cin >> x;
		v.push_back(x);
	}
	for (int i = 0; i < n; i++)
	{
		tmp = 0;
		for (int j = 2; j <= v[i]; j++)
		{
			if (v[i] % j == 0)
				tmp++;			
		}
		if (tmp == 1)
		{
			result++;
		}
	}
	cout << result;
	return 0;
}