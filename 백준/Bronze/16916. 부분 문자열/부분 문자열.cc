#include<iostream>
#include<string.h>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s, p;
	cin >> s >> p;
	if (strstr((char*)s.c_str(), (char*)p.c_str()) == NULL){
		cout << 0;
	}
	else {
		cout << 1;
	}
	return 0;
}