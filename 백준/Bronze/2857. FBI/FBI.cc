#include<iostream>
#include<string>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	string s;
	int arr[5] = { 0, };
	int temp = 0;
	for (int i = 0; i < 5; i++)
	{
		getline(cin, s);	
		if (s.find("FBI") != string::npos) {
			arr[i]= i+1;
		}
	}
	for (int i = 0; i < 5; i++)
	{
		if (arr[i] != 0) {
			cout << arr[i] <<" ";
		}
		else {
			temp++;
		}
	}
	if (temp == 5) {
		cout << "HE GOT AWAY!" << "\n";
	}
	return 0;
}