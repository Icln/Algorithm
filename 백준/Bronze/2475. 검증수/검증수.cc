#include<iostream>
using namespace std;
int main() {
	int n[5];
	int temp = 0;
	cin >> n[0] >> n[1] >> n[2] >> n[3] >> n[4];
	
	for (int i = 0; i < 5; i++){
		if (n[i]<0){
			cout << "error" << endl;
			return 0;
		}
		temp += n[i] * n[i];
	}

	cout << temp % 10 << endl;
	return 0;
}