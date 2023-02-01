#include<iostream>
using namespace std;
int main() {
	int l , p;
	int n[5];
	int r[5];
	cin >> l >>p;
	cin >> n[0] >> n[1] >> n[2] >> n[3] >> n[4];
	if (l>=1 && l<=10 && p>=1 && p<=1000)
	{
		for (int i = 0; i < 5; i++)
		{
			r[i] = n[i] - l * p;
			cout << r[i] <<" ";
		}
	}
	else {
		cout << "error" << endl;
	}
	
	return 0;
}