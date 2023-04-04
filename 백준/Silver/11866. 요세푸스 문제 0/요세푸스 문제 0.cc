#include<iostream>
#include<queue>
#include<vector>
using namespace std;
queue<int>q;
vector<int> result;
int n, k;
int cnt = 1;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> n >> k;
	if (n == 1)
	{
		cout << "<" << 1 << ">" << '\n';
		return 0;
	}
	for (int i = 1; i <= n; i++)
		q.push(i);
	while (q.size() != 1)
	{
		if (cnt % k == 0)
		{
			result.push_back(q.front());
			q.pop();
		}
		else{
			q.push(q.front());
			q.pop();
		}
		cnt++;
	}
	cout << '<';
	for (auto i : result)
	{
		cout << i << ", ";
	}
	cout << q.front() << '>';
	return 0;
}