#include <iostream>
#include <stack>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	int k, n;
	stack <int> s;
	cin >> k;
	for (int i = 0; i < k; i++)
	{
		cin >> n;
		if (n == 0)
		{
			s.pop();
		}
		else {
			s.push(n);
		}
	}
	int result = 0;
	int cnt = s.size();
	for (int i = 0; i < cnt; i++){
		result += s.top();
		s.pop();
	}
	cout << result<< '\n';
	return 0;
}