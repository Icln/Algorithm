#include<iostream>
using namespace std;
int main() {
	int r1,r2;
	int s;
	cin >> r1 >> s;
	if (r1>=-1000 && r1<=1000 && s>=-1000 && s<=1000)
	{
		r2 = s * 2 - r1;
		cout << r2 << endl;
	}
	else {
		cout << "error" << endl;
	}
	
	return 0;
}