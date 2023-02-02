#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int A, I;
	cin >> A >> I;
	if (A >= 1 && I <=100)
	{
		if (A == 1)
		{
			cout << A * I;
		}
		else
		{
			cout << A * (I - 1) + 1;
		}
	}
	else {
		cout << "error" << "\n";
	}
	return 0;
}