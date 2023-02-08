#include<iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n;
	int x = 1, y = 1;
	int temp = 2;
	cin >> n;
	for (int i = 1; i < n; i++)
	{
		if (x == 1 || y == 1)
		{
			if (x <= y)
			{
				if (y % 2 == 1)
				{
					y++;
					temp++;
				}
				else {
					x++;
					y--;
				}
			}
			else
			{
				if (x % 2 == 0)
				{
					x++;
					temp++;
				}
				else {
					x--;
					y++;
				}
			}
		}
		else {
			if (x + y == temp && temp % 2 == 0)
			{
				x --;
				y ++;
			}
			else if (x + y == temp && temp % 2 != 0)
			{
				x ++;
				y --;
			}
		}
	}
	
	cout << x << "/" << y << "\n";
	return 0;
}