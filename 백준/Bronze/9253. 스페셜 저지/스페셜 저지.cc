#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	
	string s1, s2,s3;
	cin >> s1;
	cin >> s2;
	cin >> s3;

	if (s1.find(s3) != string::npos)
	{
		if (s1.find(s3) != string::npos) {
			cout << "YES" << "\n";
		}
		else {
			cout << "NO" << "\n";
		}
	}
	else {
		cout << "NO" << "\n";
	}
}