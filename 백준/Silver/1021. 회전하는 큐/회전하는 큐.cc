#include<iostream>
#include<queue>
using namespace std;
int n, m;
int l, r;
int cnt = 0;
deque<int> dq;
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		dq.push_back(i);
	
	while (m--){
		int num;
		cin >> num;
		for (int i = 0; i < dq.size(); i++){
			if (dq[i]==num){
				l = i;
				r = dq.size() - i;
				break;
			}
		}
		if (l <= r){
			while (1){
				if (dq.front() == num) {
					dq.pop_front();
					break;
				}
				dq.push_back(dq.front());
				dq.pop_front();
				cnt++;
			}
		}
		else {
			while (1) {
				if (dq.front() == num) {
					dq.pop_front();
					break;
				}
				dq.push_front(dq.back());
				dq.pop_back();
				cnt++;

			}
		}
	}
	cout << cnt << '\n';
	return 0;
}