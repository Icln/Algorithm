#include<iostream>
using namespace std;
int main() {
	int s1,s2,s3,s4;
	
	cin >> s1;
	cin >> s2;
	cin >> s3;
	cin >> s4;

	int s = s1 + s2 + s3 + s4;
	int m = s / 60;
	s %= 60;
	if (m >= 1 && m <= 59 && s >= 0 && s<= 59)
	{
		cout << m << endl << s << endl;
	}
	else {
		cout << "error" << endl;
	}
	
	return 0;
}