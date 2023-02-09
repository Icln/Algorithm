#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	int i = 666;
	int idx = 0;
	int tmp = 0;
	cin >> n;
	while (1)
	{
		tmp = i;
		while (tmp > 0)
		{
			if (tmp % 1000 == 666)
			{
				idx++;
				if (idx == n)
				{
					cout << i;
					return 0;
				}
				break;
			}
			tmp /= 10;
		}
		i++;
	}
	return 0;
}