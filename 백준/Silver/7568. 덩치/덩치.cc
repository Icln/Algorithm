#include<iostream>
#include<vector>
using namespace std;
vector<vector<int>> v;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	int x, y;
	int cnt = 0;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		vector<int> tmp;
		cin >> x >> y;
		tmp.push_back(x);
		tmp.push_back(y);
		tmp.push_back(0);
		v.push_back(tmp);
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (v[i][0] < v[j][0])
			{
				if (v[i][1] < v[j][1])
				{
					v[i][2]++;
				}
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		cout << v[i][2] + 1 << ' ';
	}
	return 0;
}
