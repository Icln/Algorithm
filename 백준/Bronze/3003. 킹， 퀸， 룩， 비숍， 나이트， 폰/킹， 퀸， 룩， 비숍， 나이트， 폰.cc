#include<iostream>
using namespace std;
int main() {
	int n[6];
	int temp[6]={1,1,2,2,2,8};
	cin >> n[0] >> n[1] >> n[2] >> n[3] >> n[4] >> n[5];
	
	for (int i = 0; i < 6; i++){
		n[i] = temp[i] - n[i];
		cout << n[i] <<" ";
	}

	return 0;
}