#include<iostream>
#include<queue>
using namespace std;
queue<int>q;
int n;
int cnt = 1;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> n;
	if (n == 1)
	{
		cout << 1 << '\n';
		return 0;
	}
	for (int i = 1; i <= n; i++)
		q.push(i);
	while (q.size() != 1)
	{
		if (cnt % 2 == 1)
			q.pop();
		else {
			q.push(q.front());
			q.pop();
		}
		cnt++;
	}
	cout << q.front() << '\n';
	return 0;
}