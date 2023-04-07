#include<iostream>
#include<string>
#include<deque>
using namespace std;
int T;
int n;
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> T;
	for (int i = 0; i < T; i++) {
		bool error = false;
		bool reverse = false;
		string cmd;
		string arr;
		cin >> cmd;
		cin >> n;
		cin >> arr;
		deque<int> dq;
		string s;
		for (int i = 0; i < arr.length(); i++) {
			if (isdigit(arr[i])) {
				s += arr[i];
			}
			else {
				if (!s.empty()) {
					dq.push_back(stoi(s));
					s = "";
				}
			}
		}
		for (auto i : cmd)
		{
			if (i == 'R')
				reverse = !reverse;
			else {
				if (dq.empty()) {
					error = true;
					cout << "error" <<'\n';
					break;
				}
				else {
					if (reverse)
						dq.pop_back();
					else
						dq.pop_front();
				}
			}
		}
		if (!error) {
			cout << '[';
		}
		if (reverse && !dq.empty()){
			for (auto j = dq.rbegin(); j != dq.rend(); j++) {
				if (j == dq.rend() - 1)
					cout << *j;
				else
					cout << *j << ',';
			}
		}
		else if (!reverse && !dq.empty()) {
			for (auto j = dq.begin(); j != dq.end(); j++) {
				if (j == dq.end() - 1)
					cout << *j;
				else
					cout << *j << ',';
			}
		}
		if (!error)
			cout << ']' << '\n';
		
	}
	return 0;
}