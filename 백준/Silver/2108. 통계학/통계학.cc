#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
vector<int> v;
vector<pair <int, int>> vv;
bool compare(pair<int, int> v1, pair<int, int> v2) {
	if (v1.second == v2.second)
	{
		return v1.first < v2.first;
	}
	return v1.second > v2.second;
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	double n,temp, sum = 0;
	bool flag = true;
	cin >> n;
	for (int  i = 0; i < n; i++)
	{
		cin >> temp;
		v.push_back(temp);
		if (i == 0)
		{
			vv.push_back(make_pair(temp, 1));
		}
		else {
			for (int j = 0; j < vv.size(); j++)
			{
				if (vv[j].first == temp) {
					vv[j].second++;
					flag = false;
					break;
				}
			}
			if (flag)
			{
				vv.push_back(make_pair(temp,1));
			}
		}
		sum += temp;
		flag = true;
	}
	sort(v.begin(), v.end());
	sort(vv.begin(), vv.end(), compare);
	int result = round(sum / v.size());
	if (n == 1) {
		cout << result << "\n" << v[v.size() / 2] << "\n" << vv[0].first << "\n" << v.back() - v.front();
	}
	else {
		if (vv[0].second == vv[1].second)
		{
			cout<< result << "\n" << v[v.size() / 2] <<"\n" <<vv[1].first << "\n" << v.back() - v.front();
		}
		else
		{
			cout<< result << "\n" << v[v.size() / 2] << "\n" << vv[0].first << "\n" << v.back() - v.front();
		}
	}
	return 0;
}