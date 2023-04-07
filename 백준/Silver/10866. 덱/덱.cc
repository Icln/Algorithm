#include<iostream>
#include<queue>
using namespace std;
int n, tmp;
string inst;
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> n;
	deque<int> dq;
	for (int i = 0; i < n; i++)
	{
		cin >> inst;
		if (inst=="push_back")
		{
			cin >> tmp;
			dq.push_back(tmp);
		}
		else if (inst == "push_front") {
			cin >> tmp;
			dq.push_front(tmp);
		}
		else if (inst == "pop_front") {
			if (dq.empty())
				cout << -1 << '\n';
			else{
				cout << dq.front() << '\n';
				dq.pop_front();
			}
		}
		else if (inst == "pop_back") {
			if (dq.empty())
				cout << -1 << '\n';
			else{
				cout << dq.back() << '\n';
				dq.pop_back();
			}
		}
		else if (inst == "size") {
			cout << dq.size() << '\n';
		}
		else if (inst == "empty") {
			if (dq.empty())
				cout << 1 << '\n';
			else
				cout << 0 << '\n';
		}
		else if (inst == "back") {
			if (dq.empty())
				cout << -1 << '\n';
			else
				cout << dq.back() << '\n';
		}
		else if (inst == "front") {
			if (dq.empty())
				cout << -1 << '\n';
			else
				cout << dq.front() << '\n';
		}
	}
	return 0;
}