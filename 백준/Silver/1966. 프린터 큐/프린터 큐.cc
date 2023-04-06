#include<iostream>
#include<queue>
using namespace std;
int n;
int num, m;
int p;
int cnt;
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cnt = 0;
		queue <pair<int, int>> q;
		priority_queue<int> pq;
		cin >> num >> m;
		for (int j = 0; j < num; j++)
		{
			cin >> p;
			q.push({j, p});
			pq.push(p);
		}
		while (!q.empty())
		{
			int index = q.front().first;
			int value = q.front().second;
			q.pop();
			if (pq.top() == value) {
				pq.pop();
				++cnt;
				if (index == m) {
					cout << cnt << endl;
					break;
				}
			}
			else q.push({ index,value });
		}
	
	}
	return 0;
}