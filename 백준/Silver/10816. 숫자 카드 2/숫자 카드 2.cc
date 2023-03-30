#include <iostream>
#include <map>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, m, tmp;
	map <int, int> cnt;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		if (!cnt.count(tmp)){
			cnt.emplace(tmp, 1);
		}
		else {
			cnt[tmp]++;
		}
	}

	cin >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> tmp;
		cout<< cnt[tmp]<<' ';
	}
	
	return 0;
}