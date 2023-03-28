#include <iostream>
using namespace std;

int find_min(int temp, int i) {
	while (i > 0)
	{
		temp += i % 10;
		i /= 10;
	}
	return temp;
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int n, temp = 0, result = 0, cnt = 0;
	cin >> n;

	for (int i = 1; i < n; i++)
	{
		temp = i;
		if (find_min(temp, i) == n) {
			if (cnt == 0){
				result = i;
				cnt = 1;
			}
			else{
				if (i< result)
				{
					result = i;
				}
			}
			
		}
	}

	cout << result;

	return 0;
}